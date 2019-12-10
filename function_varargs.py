"""
1.当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数 （Positional Arguments）
都将被收集并汇集成一个称为“param”的元组（Tuple）。
类似地，
2.当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字
参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。

3.每一个函数都在其末尾隐含了一句 return None ，除非你写了你自己的 return 语句。
你可 以运行 print(some_function()) ，其中 some_function 函数不使用 return 语句，
就像这样：
        def some_function():
            pass
"""


def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
#   return None
print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
# 每一个函数都在其末尾隐含了一句 return None