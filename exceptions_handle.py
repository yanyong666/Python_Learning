"""
处理一组异常可以这样写（其中e代表异常的实例）：
    import sys
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = a / b
        print("您输入的两个数相除的结果是：", c )
    except (IndexError, ValueError, ArithmeticError):
        print("程序发生了数组越界、数字格式异常、算术异常之一")
    except:
        print("未知异常")
"""
# coding=utf-8


a = 10
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(e.args)
print("done")