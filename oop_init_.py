"""
在本例中，我们定义一个接受 name 参数（当然还有 self 参数）的 __init__ 方法。在这 里，我们创建了一个字段，
同样称为 name 。要注意到尽管它们的名字都是“name”，但这是 两个不相同的变量。虽说如此，但这并不会造成任何问题，
因为 self.name 中的点号意味着 这个叫作“name”的东西是某个叫作“self”的对象的一部分
而另一个 name 则是一个局部变量。
"""
# __init__ 方法会在类的对象被实例化（Instantiated）时立即运行
class Person:
    # 数据 --类的变量或类的对象变量 见104-105页
    def __init__(self, name):
        self.name = name
    # 接口 -->类的函数方法
    def say_hi(self):
        print('hello, my name is', self.name)
p = Person('YanYong')
p.say_hi()
