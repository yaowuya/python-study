age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

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
