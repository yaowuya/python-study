'''
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。

第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
'''

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for x in g:
    print(x)

'''
比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...
'''
print("-------斐波那契数列-----\n")


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


fib(10)

'''
要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
这就是定义generator的另一种方法。
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
而是一个generator：
'''


def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fibg
print(f)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
next(o)
next(o)
next(o)
# next(o)
'''
可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，
下次又继续执行。
执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
必须捕获StopIteration错误，返回值包含在StopIteration的value中：
'''

g = fibg(6)
while True:
    try:
        x = next(g)
        print("g: ", x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def testg():
    n = 1
    while n < 10:
        if (n > 5):
            yield n
        yield n * 2
        n = n + 1


for y in testg():
    print(y)
'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
'''


def triangles1(rows):
    L = [1, 1]
    if rows == 1:
        print(1)
    else:
        print([1])
        print([1,1])
        for i in range(3, rows+1):
            L.append(1)
            j = i - 2
            while j > 0:
                L[j] = L[j] + L[j - 1]
                j = j - 1
            L[0] = 1
            print(L)


triangles1(6)

def triangles():
    L = [1]
    while 1:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')