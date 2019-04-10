'''
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
'''


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(100))

'''
汉诺塔问题
'''
m = 0


def move(n, x, y):
    global m
    m += 1
    print("第%d步,将%d号盘子%s-->%s" % (m, n, x, y))


def Hanio(n, a, b, c):
    if n == 1:
        move(1, a, c)  # 将编b号为1的圆盘从A移到C
    else:
        Hanio(n - 1, a, c, b)  # 递归，把A塔上编号1~n-1的圆盘移到B上，以C为辅助塔
        move(n, a, c)  # 把A塔上编号为n的圆盘移到C上
        Hanio(n - 1, b, a, c)  # 递归，把B塔上编号1~n-1的圆盘移到C上，以A为辅助塔


Hanio(64, 'A', 'B', 'C')
