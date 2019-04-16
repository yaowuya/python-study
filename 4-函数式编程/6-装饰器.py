'''
假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。
所以，我们要定义一个能打印日志的decorator，
'''
def now():
    print('2019-4-15')

f=now
f()

print(now.__name__,f.__name__)
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s()" % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now1():
    print('2019-4-15')

now1()
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 写出来会更复杂。

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now3():
    print('2015-3-25')

now3()