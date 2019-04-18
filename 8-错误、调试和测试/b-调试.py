#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     b-调试
   Author :        zhongrf
   Date：          2019/4/17
"""
'''
需要一整套调试程序的手段来修复bug。
第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：

print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，
运行结果也会包含很多垃圾信息。

断言
凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
main()
'''
程序中如果到处充斥着assert，和print()相比也好不到哪去。
不过，启动Python解释器时可以用-O参数来关闭assert：

把print()替换为logging是第3种方式，
和assert比，logging不会抛出错误，而且可以输出到文件：
'''
# import logging
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

'''
pdb
第4种方式是启动Python的调试器pdb，让程序以单步方式运行，
可以随时查看运行状态。我们先准备好程序：
种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，

pdb.set_trace()
这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，
可以用命令p查看变量，或者用命令c继续运行：

'''
# import pdb
#
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)

'''
IDE
'''