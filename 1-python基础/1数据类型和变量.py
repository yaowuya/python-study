# 如果字符串里面有很多字符都需要转义，就需要加很多\，
# 为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

# 如果字符串内部有很多换行，
# 用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')
print(r'''hello,\n
world''')

age = 19
if int(age) >= 18:
    print('adult')
else:
    print('teenager')

a = 'ABc'
b = a
a = 'xyz'
print(b)
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数
print(10 / 3, ' ', 9 / 3)
print(10 // 3, '', 10 % 3)


# 整数
int=20;
# 浮点数
float=2.3;
print(int)
print(float)
print(pow(2,5))
print(2**5)

# 字符串
print("abc")
print('I\'m \"OK\"!')
print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')

