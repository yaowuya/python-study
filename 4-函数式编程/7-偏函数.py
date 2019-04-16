#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     7-偏函数
   Author :        zhongrf
   Date：          2019/4/16
"""
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，
# 可以降低函数调用的难度。而偏函数也可以做到这一点。
print(int('12345'))
print(int('12345', base=8), int('12345', 16))

'''
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
'''


def int2(x, base=2):
    return int(x, base)


print(int2('10000'))

'''
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
可以直接使用下面的代码创建一个新的函数int2：
'''

import functools

intTo2 = functools.partial(int, base=2)
print(intTo2('1010101'))
'''
所以，简单总结functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单

注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，
但也可以在函数调用时传入其他值：
'''
intTo2('10',base=10)

'''
最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
'''
