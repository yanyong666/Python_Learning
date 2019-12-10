# 在本案例中，当满足了某些条件时（ if i > 2 ），我们进行指定的操作（ 2*i ），以此来获 得一份新的列表。要注意到原始列表依旧保持不变。
listone = [2, 3, 4]
listtwo = [2*i for i in  listone if i>2]

print(listtwo)