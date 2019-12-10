"""
列表、元组和字符串可以看作序列（Sequence）的某种表现形式，可是究竟什么是序列，它又有什么特别之处？
"""
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'Swaroop'

# Indexing or Subscription operation
# 索引和下标操作符
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Item -3 is', shoplist[-3])
print('Item -4 is', shoplist[-4])

print('Character 0 is', name[0])

# slicing 切片运算符 前闭后开
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
print('Item start to -1 is', shoplist[:-1])

# 第三个参数为步长
print('\nItem start to end is', shoplist[::1])
print('2 step  is', shoplist[::2])
print('3 step  is', shoplist[::3])
# 超过步长则只返回第一个项目
print('4 step  is', shoplist[::4])

# 从字符串中切片
print('\n\nCharacters 1 to 3 is', name[1:3])
print('Characters 2 to end is', name[2:])
print('Characters 1 to -1 is', name[1:-1])
print('Characters start to end is', name[:])




