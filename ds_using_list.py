"""
列表list

x[index], x[index:index], x(arguments...), x.attribute ：下标、切片、调用、属性引用

(expressions...), [expressions...], {key: value...}, {expressions...} ：表示绑定或元组、表示列表、表示字典、表示集合
"""
# This my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('Thesre items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\n\nI also have to buy rice.\n')
shoplist.append('rice')
# shoplist.append(['fish', 'egg']) 你可以向列表中添加任何类型的 对象，包括数字，甚至是其它列表。但是后面的sort()不支持list与str两种实例
print('my shopping list is now', shoplist)


print('i will sort my list now')
shoplist.sort()
print('sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
