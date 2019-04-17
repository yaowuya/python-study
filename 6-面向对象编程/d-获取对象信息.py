#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     d-获取对象信息
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
首先，我们来判断对象类型，使用type()函数：
'''
print(type(123), type('str'), type(None))
print(type(abs))
'''
但是type()函数返回的是什么类型呢？它返回对应的Class类型。
如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
'''
print(type(123) == type(456), type(123) == int, type('abc') == type('123'),
      type('abc') == str, type('abc') == type(123))

'''
判断基本数据类型可以直接写int，str等，
但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
'''
import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

'''
对于class的继承关系来说，使用type()就很不方便。
我们要判断class的类型，可以使用isinstance()函数

能用type()判断的基本类型也可以用isinstance()判断：
'''


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky), isinstance(h, Dog), isinstance(h, Animal))
print(isinstance(d, Husky), isinstance(d, Dog), isinstance(d, Animal))
print(isinstance('a', str), isinstance(123, int), isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)), isinstance((1, 2, 3), (list, tuple)))

'''
如果要获得一个对象的所有属性和方法，可以使用dir()函数，
它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''

print(dir('ABC'))

'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
'''
print(len('ABC'), 'ABC'.__len__())


class my_dog(object):
    def __len__(self):
        return 100


dog = my_dog()
print(len(dog))

'''
仅仅把属性和方法列出来是不够的，
配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
'''


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'), hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'), obj.y)

'''
如果试图获取不存在的属性，会抛出AttributeError的错误：
可以传入一个default参数，如果属性不存在，就返回默认值：
'''
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

'''
也可以获得对象的方法：
'''
print(hasattr(obj, 'power'), getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())
