# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass


age = 0
if age >= 18:
    pass


# 让我们修改一下my_abs的定义，对参数类型做检查，
# 只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 给出坐标、位移和角度，就可以计算出新的新的坐标：
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，
# Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

r = move(100, 100, 60, math.pi / 6)
print(r)

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：
'''


def quadratic(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2
    elif delta == 0:
        x1 = -(b / (2 * a))
        x2 = x1
        return x1, x2
    else:
        return '方程无解'


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
