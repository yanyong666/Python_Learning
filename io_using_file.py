poem = '''\
if you like to do something 
i will tell you the programing
    use python!
'''

# 打开文件以编辑
f = open('poem.txt', 'w')
# 向文件中写文本
f.write(poem)
# close file
f.close()

# 如果没有特别指定
# 默认阅读的方式打开
f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:# # Zero length indicates EOF
        break
    print(line,end='')
#close file
f.close()

