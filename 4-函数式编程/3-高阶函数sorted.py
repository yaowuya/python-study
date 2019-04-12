'''
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
例如按绝对值大小排序：
'''

L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)

L1=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(L1)

L2=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(L2)

'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
data= [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
def by_score(t):
    return -t[1]
print(sorted(data,key=by_name))
print(sorted(data,key=by_score))