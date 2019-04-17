#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     e-实例属性和类属性
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
Student类本身需要绑定一个属性呢？可以直接在class中定义属性，
这种属性是类属性，归Student类所有
'''


class Students(object):
    name = 'Student'


s = Students()
print(s.name, Students.name)
s.name = "Mike"
print(s.name, Students.name)
del s.name
print(s.name, Students.name)

'''
从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
再使用相同的名称，访问到的将是类属性。
'''


# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
