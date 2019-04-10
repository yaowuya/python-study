name = ['xiaom', 'ls', 12, True]
for i in name:
    print(i)

print(list(range(10)))

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

x = 0
list = []
while x < 20:
    x += 1
    if x % 2 == 0:
        continue
    list.append(x)
print(list)
