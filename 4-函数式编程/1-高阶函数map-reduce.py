'''
Python内建了map()和reduce()函数。

map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
'''
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

from functools import reduce


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# 配合map()，我们就可以写出把str转换为int的函数
def charmTonum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


num = reduce(fn, map(charmTonum, '13579'))
print(num)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('4567'))


def char2num(s):
    return DIGITS[s]


def strToint(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(strToint('7890'))

'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    L=name[0].upper()+name[1:].lower()
    return L
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
def str2float(s):
    for i in range(len(s)):
        if s[i]=='.':
            break
    L=s[0:i]+s[i+1:]
    m=len(s)-i-1
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return dic[s]

    floatnum=reduce(fn,map(char2num,L))
    return floatnum/pow(10,m)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')