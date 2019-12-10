#W 主代码块中的 x 则不会受到影响
x = 50

def func(x):
    print('x is', x)
    x = 2  #  x 是我们这一函数块的局部变量
    print('changed local x to', x)

func(x)
print('x is still', x)
