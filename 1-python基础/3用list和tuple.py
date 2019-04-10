# Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。
str = ['xiaoming', '小红', 'x', 123, 6, 'daren']
print(str)
print(len(str))
print(str[2], str[0], str[5])
str.append("零零")
print(str)
print(str.pop(), str)
print(str.pop(2), str)
p = ['php', 'java']
str[1] = p
print(str)
print(str[1][0])
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
className = ('Michael', 'Bob', 'Tracy')
print(className)
t = ('a', 'b', ['A', 'B'])
t[2][0]=1
t[2][1]=0
print(t)
# tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。