"""
要想将一个对象存储到一个文件中，我们首先需要通过
open 以写入（write）二进制 （binary）模式打开文件，
然后调用 pickle 模块的 dump 函数。这一过程被称作封装 Pickling
接着，我们通过 pickle 模块的 load 函数接收返回的对象。这个过程被称作拆封 （Unpickling）
"""
import pickle

# 我们存贮相关对象的文件名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件
f = open(shoplistfile,'wb')# 以二进制写入

# 保存对象到文件
pickle.dump(shoplist,f) # 封装文件
f.close()

# del shoplist  list变量
del shoplist

# 重新打开存贮文件
f= open(shoplistfile,'rb')
# 从文件中载入对象
storedlist = pickle.load(f) # 解封
print(storedlist)

