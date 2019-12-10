
def print_max(x, y):
    '''打印两个数值中的最大数值。

    这两个数应该是整数'''
    # 转换成整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is the max')
    elif x == y:
        print('x is equal to y')
    else:
        print(y, 'is the max')

print_max(5,6)
print(print_max.__doc__)
