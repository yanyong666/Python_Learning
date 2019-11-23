# 基础
# 2.变量
# 标识符命名
# 数据类型
# 对象 Python 是强（Strongly）面向对象的，因为所有的一切都是对象， 包括数字、字符串与 函数。

# 案例：使用变量与字面常量
i = 5
print(i)
i = i + 1
print(i)
# 变量只需被赋予某一值。不需要声明或定义数据类型
print('''This is a multi-line string.
this is the second line.''')
# 逻辑行与物理行  这三句等价  在python 最好不要使用;分号 可以用\代替多行输出
i = 5; print(i);
i = 5;
print(i);
i = 5; print(i)
s = 'This is a string. \
 This continues the string.'  # 显式行连接（Explicit Line Joining）
print(s)

'''
j = 5
# 下面将会发生错误 注意行首有一个空格 # 缩进错误：意外缩进
 print('value is', j)    # IndentationError: unexpected indent # 缩进错误：意外缩进
print('I repeat, the value is', j)
'''


