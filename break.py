"""
break 语句用以中断（Break）循环语句，也就是中止循环语句的执行，即使循环条件没有 变更为 False ，
或队列中的项目尚未完全迭代依旧如此。
有一点需要尤其注意，如果你 中断 了一个 for 或 while 循环，任何相应循环中的 else 块都将不会被执行。
"""

while True:
    s = input('Enter something: ')
    if s == 'q':
        break
    print('Length of the string is', len(s))
print('Done')