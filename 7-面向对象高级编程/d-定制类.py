#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     d-定制类
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
__str__
'''


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student('Michael'))
s = Student('Michael')
s
'''
但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
这是因为直接显示变量调用的不是__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。
解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，
所以，有个偷懒的写法：__repr__ = __str__
'''

'''
__iter__
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
'''


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    # def __getitem__(self, n):
    #     a, b = 1, 1
    #     for x in range(n):
    #         a, b = b, a + b
    #     return a

    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)
'''
__getitem__
Fib实例虽然能作用于for循环，看起来和list有点像，
但是，把它当成list来使用还是不行，比如，取第5个元素：
Fib()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Fib' object does not support indexing

要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
'''
f = Fib()
print(f[0],f[1])
print(f[0:5])

'''
总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict
没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
'''

'''
__getattr__
那就是写一个__getattr__()方法，动态返回一个属性。
'''
class Student2(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr == 'age':
            return lambda: 25
s = Student2()
print(s.name,s.score)
# 返回函数也是完全可以的：
print(s.age())
'''
只有在没有找到属性的情况下，才调用__getattr__，
已有的属性，比如name，不会在__getattr__中查找。
'''

'''
__call__
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
'''
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student3('Michael')
s()
'''
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
'''
print(callable(Student3("xiaoming")),callable(max),callable([1, 2, 3]))