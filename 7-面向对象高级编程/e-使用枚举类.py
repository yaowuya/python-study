#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     e-使用枚举类
   Author :        zhongrf
   Date：          2019/4/16
"""
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，
# 或者枚举它的所有成员：
# value属性则是自动赋给成员的int常量，默认从1开始计数。

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1, Weekday.Tue, Weekday['Tue'], Weekday.Tue.value)
print(print(Weekday(1)))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

'''
把Student的gender属性改造为枚举类型，可以避免使用字符串：
'''
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student4(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student4('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')