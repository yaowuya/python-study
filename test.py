# print('hello')
# print('hello, world', '小明', 'hi')
# print(100*200+2)
# name=input("please enter your name: ")
# print("hello,",name)

# one=input("please input firstnum: ")
# two=input("please input secondnum: ")
# print(int(one),"*",int(two),"=",int(one)*int(two))
# L=[1,2,3,4]
# print([L[i] + L[i + 1] for i in range(3)])
#
# for i in L:
#     pass
# print(i)

# L=[{"name":"123","age":123},{"name":"45","age":123}]
# print(L)

# a=1 # 变量a是一个整数
# Answer = True #变量Answer是一个布尔值True。

# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)


# # 整数
# int=20;
# # 浮点数
# float=2.3;
# print(int)
# print(float)
# print(pow(2,5))
# print(2**5)
"""
用户身份验证
"""
username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
