#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     a-类和实例
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
面向对象最重要的概念就是类（Class）和实例（Instance），
必须牢记类是抽象的模板，比如Student类，
而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，
但各自的数据可能不同。
'''


class Student(object):
    pass


'''
class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
'''

bar = Student()
print(bar, Student)
bar.name = "xiaoming"
print(bar.name)
'''
由于类可以起到模板的作用，因此，可以在创建实例的时候，
把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

注意：特殊方法“__init__”前后分别有两个下划线！！！
'''


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" %(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bar=Student("mike",19)

print(bar.name,bar.score)
print(bar.print_score())
print(bar.get_grade())
