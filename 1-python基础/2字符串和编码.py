# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，
# chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(65))
print(ord('中'))
print(chr(20013))
'''
以Unicode表示的str通过encode()方法可以编码为指定的bytes
Python对bytes类型的数据用带b前缀的单引号或双引号表示
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，
应当始终坚持使用UTF-8编码对str和bytes进行转换。
'''
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换
print('hello %s,you have $%d' % ('mike', 1000))
# % 2d是将数字按宽度为2，采用右对齐方式输出，如果数据位数不到2位，则左边补空格
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 小明的成绩从去年的72分提升到了今年的85分，
# 请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
s1 = input("请输入上一年的成绩：")
s2 = input("请输入今年的成绩：")
name = input("请输入名字：")
a = float(s1)
b = float(s2)
r = ((b - a) / a) * 100
if a == b:
    print("%s,您的成绩非常稳定" % (name))
elif a < b:
    print("恭喜%s,您的成绩提升了%.1f%%" % (name, r))
else:
    r = -r
    print("%,很遗憾，您的成绩下降了%.1f%%" % (name, r))
