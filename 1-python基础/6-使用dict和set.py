# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Michael']=66
print(d)
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
d['Jack'] = 88
print(d)
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Michael'),d.get('Michael1',-1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d.pop("Tracy"))
d["Obj"]=98
print(d)

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。

# 要创建一个set，需要提供一个list作为输入集合,重复元素在set中自动被过滤，显示的顺序不表示set是有序的
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(6)
# 通过remove(key)方法可以删除元素
s.remove(3)
print(s)

s2 = set([2, 3, 4])
# set可以看成数学意义上的无序和无重复元素的集合，因此，
# 两个set可以做数学意义上的交集、并集等操作
print(s&s2,s|s2)

s3=set()
s3.add("a")
print(s3)

bb=None
if bb is None:
    print(bb)