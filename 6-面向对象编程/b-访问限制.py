#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     b-访问限制
   Author :        zhongrf
   Date：          2019/4/16
"""
'''
在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，
这样，就隐藏了内部的复杂逻辑。

从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
'''


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


'''
改完后，对于外部代码来说，没什么变动，
但是已经无法从外部访问实例变量.__name和实例变量.__score了
'''
bart = Student("mike", 88)

'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，
比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量：

总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
'''
print(bart._Student__name)
'''
请把下面的Student对象的gender字段对外隐藏起来，
用get_gender()和set_gender()代替，并检查参数有效性：
'''


class StudentDemo(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender


# 测试:
b = StudentDemo('Bart', 'male')
if b.get_gender() != 'male':
    print('测试失败!')
else:
    b.set_gender('female')
    if b.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
