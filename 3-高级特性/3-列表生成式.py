'''
列表生成式即List Comprehensions，
是Python内置的非常简单却强大的可以用来创建list的生成式

写列表生成式时，把要生成的元素x * x放到前面，
后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
'''
L = [x * x for x in range(1, 11)]
print(L)

L1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L1)

'''
还可以使用两层循环，可以生成全排列：
'''
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(L3)

# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

dir = [d for d in os.listdir()]
print(dir)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，
所以列表生成式会报错
使用内建的isinstance函数可以判断一个变量是不是字符串：
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''

ListData = ['Hello', 'World', 18, 'Apple', None]
List2 = [x.lower() for x in ListData if isinstance(x, str)]
print(List2)
