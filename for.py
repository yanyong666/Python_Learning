"""
for...in 语句是另一种循环语句，其特点是会在一系列对象上进行迭代（Iterates），意即 它会遍历序列中的每一个项目。
"""
for i in range(1,5):
    print(i)
else:
    print('the for loop is over')  #   else 部分是可选的。当循环中包含他时，它总会在 for 循环结束后开始执 行，除非程序遇到了 break 语句。
print(list(range(0, 5)))
print(list(range(1, 5)))
print(list(range(1, 5, 2)))