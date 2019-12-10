"""
while 语句能够让你在条件为真的前提下重复执行某块语句。
while 语句是 循环 （Looping） 语句的一种。
while 语句同样可以拥有 else 子句作为可选选项。
"""

# 设置变量
number = 23

running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将会导致while 终止
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
        # 如果 while 循环中存在一个 else 代码块，它将总是被执行， 除非你通过 break 语句来中断这一循环
    #   break
else:
    print('The while loop is over.')
print('Done')
