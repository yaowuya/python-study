#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     1-模块
   Author :        zhongrf
   Date：          2019/4/12
"""
import sys

def test():
    args=sys.argv
    if len(args)==1:
        print("Hello world",args)
    elif len(args)==2:
        print("Hello %s!" %args[1])
    else:
        print("Too many arguments！")

if __name__ =='__main__':
    test()
    

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()

'''
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），
不应该被直接引用，比如_abc，__abc等；

，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
是因为Python并没有一种方法可以完全限制访问private函数或变量，
但是，从编程习惯上不应该引用private函数或变量。
'''
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



