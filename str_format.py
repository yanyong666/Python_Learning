# 基础
# 1.各种常量 字符串 转义字符 格式化 等等
# 格式化方法 python 索引从0开始 转换至字符串的工作将由 format 方法自动完成
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('why id {0} playing with that python'.format(name))
# this is not a good idea 明确转换至字符串
print(name + ' is ' + str(age) +  ' years old')

# Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置。这之中可以有 更详细的格式
# 对于浮点数 '0.333' 保留小数点后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本
# 使用（^）定义'__hello__'字符串长度11
print('{0:_^11}'.format('hello'))

# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

# print 总默认以一个不可见的新的一行字符（\n）结尾
print('a', end='')
print('b', end='')
print('')
# 转义序列（Escape Sequence）
# 转义序列 \\ 来指定反斜杠本身
# 新一行的转义序列—— \n
# 的转义序列是制表符： \t
print('what\'s your name')
print("what's your sex")
print(
'''这是一段多行字符串。这是它的第一行。 
This is the second line. 
"What's your name?," I asked.
 He said "Bond, James Bond." 
 ''')
print('this is the first line\nthis is the second line')
print('this is the first line\tthis is the second line')
print("this is the first sentence.\
 this is the second sentence") #放置在末尾的反斜杠表示字符串将在下一行继 续，但不会添加新的一行
# 输出原始未经过处理的字符串 比如转义字符\n 在前面加r或者R
print(r"Newlines are indicated by \n")









