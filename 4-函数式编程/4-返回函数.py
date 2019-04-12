'''
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())
'''
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

'''
利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''
def createCounter():
    a=0
    def counter():
        nonlocal a
        a+=1
        return a
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')