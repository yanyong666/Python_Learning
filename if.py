'''
if 语句用以检查条件：如果 条件为真（True），我们将运行一块语句（称作 if-block 或 if 块），
否则 我们将运行另一块语句（称作 else-block 或 else 块）。其中 else 从句是可选 的。
'''

# 设置变量
number = 23
# input() 函数来获取用户 的猜测数
guess = int(input('Enter an integer: '))   # int 将这个字符串转换成一个整数并将其储存在变量 guess 中

# if条件语句
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it. ')
    print('(but you do ont win any prizes!)')
    # 新块从这里结束
elif guess < number:
    # 另一代码块
    print('No,it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No,it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')
# 这最后一句将在
# if 语句执行完毕后执行
