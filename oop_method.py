#能看见 self 是如何行动的了。要注意到 say_hi 这一方法不需要参数，但是依 旧在函数定义中拥有 self 变量# # 。
class Person:
  def say_hi(self):
        print('hello, how are you ？')

# 类实体变量=对象
p = Person()
p.say_hi()
#面两行同样可以写作
# Person().say_hi()



