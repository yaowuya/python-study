#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   File Name：     d-序列化
   Author :        zhongrf
   Date：          2019/4/18
"""
'''
我们把变量从内存中变成可存储或传输的过程称之为序列化
在Python中叫pickling
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。     
'''
import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
'''
pickle.dumps()方法把任意对象序列化成一个bytes，
然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
我们打开另一个Python命令行来反序列化刚才保存的对象：
'''
fb=open('dump.txt','rb')
data=pickle.load(fb)
fb.close()
print(data)
'''
Pickle的问题和所有其他编程语言特有的序列化问题一样，
就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''
'''
JSON
dumps()方法返回一个str，内容就是标准的JSON。
类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

'''
print("-"*30)
import json
j = dict(name='Bob', age=20, score=88)
print(json.dumps(j))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('test', 20, 88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))

'''
不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。
我们可以偷个懒，把任意class的实例变为dict：

print(json.dumps(s, default=lambda obj: obj.__dict__))
'''

'''
同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例：
'''
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))