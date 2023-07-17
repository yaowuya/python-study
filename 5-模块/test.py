# from module1 import foo

# # 输出hello, world!
# foo()

# from module2 import foo

# # 输出goodbye, world!
# foo()

# 也可以按照如下所示的方式来区分到底要使用哪一个foo函数。

# import module1 as m1
# import module2 as m2
# m1.foo()
# m2.foo()

from module1 import foo
foo()