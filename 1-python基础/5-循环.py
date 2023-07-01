# name = ['xiaom', 'ls', 12, True]
# for i in name:
#     print(i)

# print(list(range(10)))

"""
用for循环实现1~100求和
"""
sum = 0
for x in list(range(101)):
    sum += x
print(sum)
# 我们要计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# 如果我们想只打印奇数

# x = 0
# list = []
# while x < 20:
#     x += 1
#     if x % 2 == 0:
#         continue
#     list.append(x)
# print(list)


"""
猜数字游戏
下面我们通过一个“猜数字”的小游戏来看看如何使用while循环。
猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')