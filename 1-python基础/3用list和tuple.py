# Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# 变量classmates就是一个list。用len()函数可以获得list元素的个数
print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0], classmates[1], classmates[2])
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
# 以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-2],classmates[-3])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)
# list里面的元素的数据类型也可以不同
list_tmp = ['Apple', 123, True]
p = ['php', 'java']
list_tmp[1] = p
print(list_tmp)
print(list_tmp[1][0])


# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
className = ('Michael', 'Bob', 'Tracy')
print(className)
# classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)
# 如果要定义一个空的tuple，可以写成()
t = ()
print(t)
# 但是，只有1个元素的tuple定义时必须加一个逗号,
t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0]=1
t[2][1]=0
print(t)
# tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。

List=[1,2,3]
List.remove(3)
print(List)



