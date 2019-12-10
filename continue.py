"""
continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭 代。
"""
while True:
    s = input('Enter something: ')
    if s == 'q':
        break
    if len(s) < 3:
        print('too small')
        continue
        print('i am not done')
    print('Input is of sufficient length')
