#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     a-使用__slots__
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
'''


class Student(object):
    __slots__ = ("name", "age")


s = Student()
s.name = "Mike"
s.age = 18
# s.score=99
'''
由于'score'没有被放到__slots__中，所以不能绑定score属性，
试图绑定score将得到AttributeError的错误。
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，
对继承的子类是不起作用的：
'''
print(s.name)


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 99

print(g.score)
