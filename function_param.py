def print_max(a, b):
    if a > b:
        print(a, 'is maxinum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maxinum')
# 直接传递函数参数值
print_max(3,4)

x = 5
y =7
# 以参数的形式传递变量
print_max(x,y)
print(x, y) # 全局变量不受局部影响


def print_min(a, b):
    if a < b:
        print(a, 'is the min')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is the min')

# 直接传递实参
print_min(3,4)

# 以变量当做实数形式传递 #  print_max(x, y) 将使得实参 x 的值将被赋值给形参 a ，而实参 y 的值将被赋值给形参 b
x = 15
y = 17
print_min(x, y)
print(x, y)

