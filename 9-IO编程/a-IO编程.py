#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     a-IO编程
   Author :        zhongrf
   Date：          2019/4/18
"""
'''
读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
'''
try:
    f=open('./test.txt','r',encoding='utf-8')
    data = f.read()
    print(data)
finally:
    if f:
        f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open('./test.txt','r',encoding='utf-8') as f:
    print(f.read())

'''
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，
调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；如果不能确定文件大小，
反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

'''
with open('./test.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())# 把末尾的'\n'删掉

'''
二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
'''
j=open('./test.jpg','rb')
print(j.read())
'''
字符编码
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，
例如，读取GBK编码的文件：
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，
open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
最简单的方式是直接忽略：

'''
g=open('./gbk.txt','r',encoding='gbk',errors='ignore')
print(g.read())

'''
写文件
写文件和读文件是一样的，唯一区别是调用open()函数时，
传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
'''
w=open('./test.txt','w',encoding='utf-8')
w.write("Hello world")
w.close()

with open('./test.txt', 'w',encoding='utf-8') as g:
    g.write('Hello, world!')

'''
细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，
会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？
可以传入'a'以追加（append）模式写入
'''
'''
请将本地一个文本文件读为一个str并打印出来：
'''
fpath = r'./requirements.txt'
with open(fpath,'r',encoding='utf-8') as f:
    s=f.read(20)
    while s:
        print(s, end='\n')
        s = f.read(20)

with open(fpath,'r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line)