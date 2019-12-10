name = 'Swaroop'
#  startswith 方法用于查找字符串是 否以给定的字符串内容开头
if name.startswith('Swa'):
    print('yes, the string starts with "Swa"')

if 'a' in name:
    print('yes, it contains the string "a"')

# find 方法用于定位字符串中给定的子字符串的位置
if name.find('war') != -1:
    print('Yes, it contains the string "war"')

if name.find(name[1:4]) != -1:
    print('Yes, it contains the string ', name[1:4])

#  str 类同样还拥有一个简洁的方法用以 联结（Join） 序列(list也是一种序列)中的项目
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))