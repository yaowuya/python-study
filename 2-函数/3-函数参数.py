'''
位置参数
修改后的power(x, n)函数有两个参数：x和n，
 这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
'''


def my_power(x, n):
    s = 1;
    while n > 0:
        n = n - 1
        s *= x
    return s


my_power(2, 3)

'''
默认参数
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
变化小的参数就可以作为默认参数。
定义默认参数要牢记一点：默认参数必须指向不变对象！
'''


def my_power2(x, n=2):
    s = 1;
    while n > 0:
        n = n - 1
        s *= x
    return s


my_power2(5)
my_power2(5, 3)


def enroll(name, gender, age=6, city="beijin"):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Adam', 'M', city='Tianjin')


def add_end(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


add_end()
add_end()

'''
可变参数
在Python函数中，还可以定义可变参数。顾名思义，
可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，
因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
'''


def calc(*number):
    s = 0;
    for num in number:
        s += num * num
    return s


calc(1, 2)
calc(3)
'''
所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
'''
num = [1, 2, 3]
calc(*num)

'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict
'''


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("xiaoming", 6)
person('Adam', 45, gender='M', job='Engineer')
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
对kw的改动不会影响到函数外的extra。
'''
extra = {'city': 'Beijing', 'job': 'Engineer'}
person("Jack", 24, **extra)

'''
命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数，
例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
*后面的参数被视为命名关键字参数。
'''


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Engineer')

'''
如果函数定义中已经有了一个可变参数，
后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
'''


def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


'''
参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。但是请注意，
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2, 3, 'a', 'b', x=99)

f2(1, 2, d=99, ext=None)

'''
所以，对于任意函数，
都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
'''
args = (1, 2, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

'''
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
'''


def product(*args):
    s = 1
    if len(args) == 0:
        raise TypeError("不能为空")
    for i in args:
        s= s * i
    return s


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
