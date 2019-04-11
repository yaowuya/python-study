d = {'a': 3, 'b':4, 'c':7}
for key in d:
    print(key)

for key, value in d.items():
    print(key, value)

for ch in 'ABCDEf':
    print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

'''
最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身：
'''
L = ['1', 2, '3', True]
for i, value in enumerate(L):
    print(i, value)

for i, value in enumerate(d):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
data = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in data.items():
    print(k, '=', v)

'''
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for value in L:
        if (min > value):
            min = value
        if (max < value):
            max = value
    return min, max
print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7, 1]))
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')