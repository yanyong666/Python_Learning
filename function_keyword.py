def func(a, b=5 ,c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3,7)

# 关键字参数c指定了c=24
func(25,c=24)

# 关键字参数c指定了50 ，a指定了100 尽管a在c定义
func(c=50, a=100)