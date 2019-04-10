'''
L[0:3]表示，从索引0开始取，直到索引3为止，
但不包括索引3。即索引0，1，2，正好是3个元素。
'''
L = list(range(100))
# 可以通过切片轻松取出某一段数列。比如前10个数：
print(L[:10])
# 后10个数：
print(L[-10:])
# 前10个数，每两个取一个：
print(L[:10:2])
print(L[::5])

print((0, 1, 2, 3, 4, 5)[:3])
# 字符串切片
print('ABCDEFG'[:3])

'''
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
'''


def trim(str):
    if str == "":
        return str
    while str[:1] is ' ':
        str = str[1:]
    while str[-1:] is ' ':
        str = str[:-1]
    return str


print(trim('hello  '))
print(trim('  hello  '))
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
