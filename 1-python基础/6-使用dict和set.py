# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Michael']=66
print(d)
print(d.get('Michael'),d.get('Michael1',-1))
print(d.pop("Tracy"))
d["Obj"]=98
print(d)

# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(6)
s.remove(3)
print(s)
s2 = set([2, 3, 4])
# set可以看成数学意义上的无序和无重复元素的集合，因此，
# 两个set可以做数学意义上的交集、并集等操作
print(s&s2,s|s2)