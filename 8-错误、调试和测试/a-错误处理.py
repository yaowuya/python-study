#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     a-错误处理
   Author :        zhongrf
   Date：          2019/4/17
"""
'''
高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
但是finally如果有，则一定会被执行（可以没有finally语句）。
'''
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
'''
此外，如果没有错误发生，可以在except语句块后面加一个else，
当没有错误发生时，会自动执行else语句：
'''
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

'''
使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
这时，只要main()捕获到了，就可以处理：
'''


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()

'''
记录错误
Python内置的logging模块可以非常容易地记录错误信息：
'''
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

'''
抛出错误
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，
然后，用raise语句抛出一个错误的实例：
'''
# class FooError(ValueError):
# #     pass
# #
# # def foo(s):
# #     n = int(s)
# #     if n==0:
# #         raise FooError('invalid value: %s' % s)
# #     return 10 / n
# #
# # # foo('0')
# #
# # def foo1(s):
# #     n = int(s)
# #     if n==0:
# #         raise ValueError('invalid value: %s' % s)
# #     return 10 / n
# #
# # def bar1():
# #     try:
# #         foo1('0')
# #     except ValueError as e:
# #         print('ValueError!')
# #         raise
# #
# # bar1()

from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()