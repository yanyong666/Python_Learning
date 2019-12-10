"""
元组tuple

x[index], x[index:index], x(arguments...), x.attribute ：下标、切片、调用、属性引用

(expressions...), [expressions...], {key: value...}, {expressions...} ：表示绑定或元组、表示列表、表示字典、表示集合
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。

"""
zoo = ('python', 'elephant', 'penguin')

print('number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
#new_zoo = ('monkey', 'camel', zoo)
print('number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)

print('Animals brought from old zoo are', new_zoo[2])
print('First animal brought from old zoo is', new_zoo[2][0])
print('Sencond brought from old zoo is', new_zoo[2][1])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))
