"""
x[index], x[index:index], x(arguments...), x.attribute ：下标、切片、调用、属性引用

(expressions...), [expressions...], {key: value...}, {expressions...} ：表示绑定或元组、表示列表、表示字典、表示集合
"""

# “ab”是地址（Address）簿（Book）的缩写
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值-值配对
del ab['Spammer']

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

# 字典ab的方法items()调用返回的是一份包含元组的列表
print(ab.items(),'\n')

for name, address in ab.items():
    print('Contacts {} at {}'.format(name, address))

# 添加一对键值-值配对  我们可以简单地通过使用索引运算符访问一个键值并为 其分配与之相应的值
ab['yanyong'] = 'yy@python.org'

if 'yanyong' in ab:
    print("\nyanyong's address is", ab['yanyong'],'\n')

for name, address in ab.items():
    print('Contacts {} at {}'.format(name, address))