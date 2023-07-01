# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# if判断条件还可以简写，只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x=True
if x:
    print('True')
    
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


'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
height = float(input('请输入身高(m)：'))
weight = float(input('请输入体重(kg)：'))
r = weight / pow(height, 2)
if r < 18.5:
    print("您的BMI值为：%.1f,体重过轻" % r)
elif r >= 18.5 and r < 25:
    print("您的BMI值为：%.1f,体重正常" % r)
elif r >= 25 and r < 28:
    print("您的BMI值为：%.1f,体重过重" % r)
elif r >= 28 and r < 32:
    print("您的BMI值为：%.1f,体重肥胖" % r)
else:
    print("您的BMI值为：%.1f,严重肥胖" % r)