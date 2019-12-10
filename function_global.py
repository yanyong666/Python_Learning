x = 55

def func():
    global x # 将 x 定义 成全局变量

    print('x is', x)
    x = 5
    print('changed global x to', x)

func()
print('value of x is', x)
