'''
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，
再利用变量来调用该函数：
'''

L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)

f = lambda x: x * x
print(f(5))


# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

L2=list(filter(lambda x:x%2==1,range(1,20)))

print(L)
print(L2)
