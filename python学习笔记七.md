>微信公众号： 点击蓝色字体<font color=blue size=2.5>小白图像与视觉</font>进行关注
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言

# 下面主要讲面向对象编程
------------------------------
> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想

[TOC]


### 面向对象编程 {#oop}

类与对象是面向对象编程的两个主要方面。一个**类（Class）**能够创建一种新的_类型（Type）_，其中**对象（Object）**就是类的**实例（Instance）**。可以这样来类比：你可以拥有类型 `int` 的变量，也就是说存储整数的变量是 `int` 类的实例（对象）。


对象可以使用_属于_它的普通变量来存储数据。这种从属于对象或类的变量叫作**字段（Field）**。对象还可以使用_属于_类的函数来实现某些功能，这种函数叫作类的**方法（Method）**。这两个术语很重要，它有助于我们区分函数与变量，哪些是独立的，哪些又是属于类或对象的。总之，字段与方法通称类的**属性（Attribute）**。

字段有两种类型——它们属于某一类的各个实例或对象，或是从属于某一类本身。它们被分别称作**实例变量（Instance Variables）**与**类变量（Class Variables）**。

通过 `class` 关键字可以创建一个类。这个类的字段与方法可以在缩进代码块中予以列出。

### `self` {#self}

类方法与普通函数只有一种特定的区别——前者必须多加一个参数在参数列表开头，这个名字必须添加到参数列表的开头，但是你*不用*在你调用这个功能时为这个参数赋值，Python 会为它提供。这种特定的变量引用的是对象_本身_，按照惯例，它被赋予 `self` 这一名称。

尽管你可以为这一参数赋予任何名称，但是_强烈推荐_你使用 `self` 这一名称——其它的任何一种名称绝对会引人皱眉。使用一个标准名称能带来诸多好处——任何一位你的程序的读者能够立即认出它，甚至是专门的 IDE（Integrated Development Environments，集成开发环境）也可以为你提供帮助，只要你使用了 `self` 这一名称。

> **针对 C++/Java/C# 程序员的提示**
> 
> Python 中的 `self` 相当于 C++ 中的 `this` 指针以及 Java 与 C# 中的 `this` 引用。

你一定会在想 Python 是如何给 `self` 赋值的，以及为什么你不必给它一个值。一个例子或许会让这些疑问得到解答。假设你有一个 `MyClass` 的类，这个类下有一个实例 `myobject`。当你调用一个这个对象的方法，如 `myobject.method(arg1, arg2)` 时，Python 将会自动将其转换成 `MyClass.method(myobject, arg1, arg2)`——这就是 `self` 的全部特殊之处所在。

这同时意味着，如果你有一个没有参数的方法，你依旧必须拥有一个参数——`self`。

### 类 {#class}

最简单的类（Class）可以通过下面的案例来展示（保存为 `oop_simplestclass.py`）：

<pre><code class="lang-python">#字段有两种类型——它们属于某一类的各个实例或对象，或是从属于某一类本身.
# 它们被分别称作实例变量（Instance Variables）与类变量（Class Variables）。
class Person:
    pass  # 一个空的代码块

### 类实体变量
p = Person()

print(p)
</code></pre>

输出：

<pre><code><__main__.Person object at 0x000000000214B588></code></pre>
**它是如何工作的**

我们通过使用 `class` 语句与这个类的名称来创建一个新类。在它之后是一个缩进的语句块，代表这个类的主体。在本案例中，我们创建的是一个空代码块，使用 `pass` 语句予以标明。



为了验证我们的操作是否成功，我们通过直接将它们打印出来来确认变量的类型。结果告诉我们我们在 `Person` 类的 `__main__` 模块中拥有了一个实例。

要注意到在本例中还会打印出计算机内存中存储你的对象的地址。案例中给出的地址会与你在你的电脑上所能看见的地址不相同，因为 Python 会在它找到的任何空间来存储对象。

### 方法method

我们已经在前面讨论过类与对象一如函数那般都可以带有方法（Method），唯一的不同在于我们还拥有一个额外的 `self` 变量。现在让我们来看看下面的例子（保存为 `oop_method.py`）。

<pre><code class="lang-python">#能看见 self 是如何行动的了。要注意到 say_hi 这一方法不需要参数，但是依 旧在函数定义中拥有 self 变量# # 。
class Person:
  def say_hi(self):
        print('hello, how are you ？')

# 类实体变量=对象
p = Person()
p.say_hi()
#面两行同样可以写作
# Person().say_hi()
</code></pre>

输出：

<pre><code>hello, how are you ？</code></pre>
**它是如何工作的**

这里我们就能看见 `self` 是如何行动的了。要注意到 `say_hi` 这一方法不需要参数，但是依旧在函数定义中拥有 `self` 变量。

### `__init__` 方法 {#init}

在 Python 的类中，有不少方法的名称具有着特殊的意义。现在我们要了解的就是 `__init__` 方法的意义。

`__init__` 方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以对任何你想进行操作的目标对象进行*初始化（Initialization）*操作。这里你要注意在 init 前后加上的双下划线。

案例（保存为 `oop_init.py`）：

<pre><code class="lang-python">"""
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
</code></pre>

输出：

<pre><code>hello, my name is YanYong</code></pre>
**它是如何工作的**

在本例中，我们定义一个接受 `name` 参数（当然还有 `self` 参数）的 `__init__` 方法。在这里，我们创建了一个字段，同样称为 `name`。要注意到尽管它们的名字都是“name”，但这是两个不相同的变量。虽说如此，但这并不会造成任何问题，因为 `self.name` 中的点号意味着这个叫作“name”的东西是某个叫作“self”的对象的一部分，而另一个 `name` 则是一个局部变量。由于我们已经如上这般明确指出了我们所指的是哪一个名字，所以它不会引发混乱。

当我们在 `Person` 类下创建新的实例 `p` 时，我们采用的方法是先写下类的名称，后跟括在括号中的参数，形如：`p = Person('Swaroop')`。

我们不会显式地调用 `__init__` 方法。
这正是这个方法的特殊之处所在。

现在，我们可以使用我们方法中的 `self.name` 字段了，使用的方法在 `say_hi` 方法中已经作过说明。

### 类变量与对象变量 {#class-obj-vars}

**类变量（Class Variable）**是共享的（Shared）——它们可以被属于该类的所有实例访问。该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现。

**对象变量（Object variable）**由类的每一个独立的对象或实例所拥有。在这种情况下，每个对象都拥有属于它自己的字段的副本，也就是说，它们不会被共享，也不会以任何方式与其它不同实例中的相同名称的字段产生关联。下面一个例子可以帮助你理解（保存为 `oop_objvar.py`）：

<pre><code class="lang-python">#codding = UTF-8

class Robot:
    """表示有一个带有名字的机器人"""
    population = 0
    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

    # 当有人被创建时，机器人数量人口增加
        Robot.population +=1
    def __del__(self):
        """机器人挂了"""
        print("{} is being destroyed!".format(self.name))
    
        Robot.population -= 1
    
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are the still {:d} robots working.".format(Robot.population))
    
    def die(self):
        """机器人挂了"""
        print("{} is being destroyed!".format(self.name))
    
        Robot.population -=1
    
        if Robot.population ==0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are the still {:d} robots working.".format(Robot.population))
    
    def say_hi(self):
        """来自机器人的诚挚问候"""
        print("Greetings,my masters call me {}.".format(self.name))
    
    # @classmethod
    # def how_manny(cls):
    #     """打印当前的机器人数量"""
    #     print("we have {:d} robots.".format(cls.population))
    @staticmethod
    def how_manny():
        print("we have {:d} robots.".format(Robot.population))

droid1 = Robot("R1-D1")
droid1.say_hi()
Robot.how_manny()

droid2 = Robot("R2-D2")
droid2.say_hi()
Robot.how_manny()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

droid1.die()
# 等价于
# del droid1
droid2.die()
# 等价于
# del droid2
Robot.how_manny()
</code></pre>

输出：

<pre><code>(Initializing R1-D1)
Greetings,my masters call me R1-D1.
we have 1 robots.
(Initializing R2-D2)
Greetings,my masters call me R2-D2.
we have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.
R1-D1 is being destroyed!
There are the still 1 robots working.
R2-D2 is being destroyed!
R2-D2 was the last one.
we have 0 robots.
R1-D1 is being destroyed!
There are the still -1 robots working.
R2-D2 is being destroyed!
There are the still -2 robots working.</code></pre>

**它是如何工作的**

这是一个比较长的案例，但是它有助于展现类与对象变量的本质。在本例中，`population` 属于 `Robot` 类，因此它是一个类变量。`name` 变量属于一个对象（通过使用 `self` 分配），因此它是一个对象变量。

因此，我们通过 `Robot.population` 而非 `self.population` 引用 `population` 类变量。我们对于 `name` 对象变量采用 `self.name` 标记法加以称呼，这是这个对象中所具有的方法。要记住这个类变量与对象变量之间的简单区别。同时你还要注意当一个对象变量与一个类变量名称相同时，类变量将会被隐藏。

除了 `Robot.popluation`，我们还可以使用 `self.__class__.population`，因为每个对象都通过 `self.__class__` 属性来引用它的类。

`how_many` 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个 `classmethod（类方法）` 或是一个 `staticmethod（静态方法）`，这取决于我们是否需要知道这一方法属于哪个类。由于我们已经引用了一个类变量，因此我们使用 `classmethod（类方法）`。

我们使用[装饰器（Decorator）](./18.more.md#decorator)将 `how_many` 方法标记为类方法。

你可以将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式，因此启用 `@classmethod` 装饰器等价于调用：

```python
how_many = classmethod(how_many)
```

你会观察到 `__init__` 方法会使用一个名字以初始化 `Robot` 实例。在这一方法中，我们将 `population` 按 1 往上增长，因为我们多增加了一台机器人。你还会观察到 `self.name` 的值是指定给每个对象的，这体现了对象变量的本质。

你需要记住你*只能*使用 `self` 来引用同一对象的变量与方法。这被称作*属性引用（Attribute Reference）*。

在本程序中，我们还会看见针对类和方法的 *文档字符串（DocStrings）* 的使用方式。我们可以在运行时通过 `Robot.__doc__` 访问类的 文档字符串，对于方法的文档字符串，则可以使用 `Robot.say_hi.__doc__`。

在 `die` 方法中，我们简单地将 `Robot.population` 的计数按 1 向下减少。

所有的类成员都是公开的。但有一个例外：如果你使用数据成员并在其名字中_使用双下划线作为前缀_，形成诸如 `__privatevar` 这样的形式，Python 会使用名称调整（Name-mangling）来使其有效地成为一个私有变量。

因此，你需要遵循这样的约定：任何在类或对象之中使用的变量其命名应以下划线开头，其它所有非此格式的名称都将是公开的，并可以为其它任何类或对象所使用。请记得这只是一个约定，Python 并不强制如此（除了双下划线前缀这点）。

> **针对 C++/Java/C# 程序员的提示**
> 
> 所有类成员（包括数据成员）都是_公开的_，并且 Python 中所有的方法都是_虚拟的（Virtual）_。

### 继承

面向对象编程的一大优点是对代码的**重用（Reuse）**，重用的一种实现方法就是通过**继承（Inheritance）**机制。继承最好是想象成在类之间实现**类型与子类型（Type and Subtype）**关系的工具。

现在假设你希望编写一款程序来追踪一所大学里的老师和学生。有一些特征是他们都具有的，例如姓名、年龄和地址。另外一些特征是他们独有的，一如教师的薪水、课程与假期，学生的成绩和学费。

你可以为每一种类型创建两个独立的类，并对它们进行处理。但增添一条共有特征就意味着将其添加进两个独立的类。这很快就会使程序变得笨重。

一个更好的方法是创建一个公共类叫作 `SchoolMember`，然后让教师和学生从这个类中_继承（Inherit）_，也就是说他们将成为这一类型（类）的子类型，而我们就可以向这些子类型中添加某些该类独有的特征。

这种方法有诸多优点。如果我们增加或修改了 `SchoolMember` 的任何功能，它将自动反映在子类型中。举个例子，你可以通过简单地向 SchoolMember 类进行操作，来为所有老师与学生添加一条新的 ID 卡字段。不过，对某一子类型作出的改动并不会影响到其它子类型。另一大优点是你可以将某一老师或学生对象看作 `SchoolMember` 的对象并加以引用，这在某些情况下会大为有用，例如清点学校中的成员数量。这被称作**多态性（Polymorphism）**，在任何情况下，如果父类型希望，子类型都可以被替换，也就是说，该对象可以被看作父类的实例。

同时还需要注意的是我们重用父类的代码，但我们不需要再在其它类中重复它们，当我们使用独立类型时才会必要地重复这些代码。

在上文设想的情况中，`SchoolMember` 类会被称作**基类（Base Class）**或是**超类（Superclass）**。`Teacher` 和 `Student` 类会被称作**派生类（Derived Classes）**或是**子类（Subclass）**。

我们将通过下面的程序作为案例来进行了解（保存为 `oop_subclass.py`）：

<pre><code class="lang-python"># coding= UTF-8

class SchoolMember:
    """代表学校里面任何成员"""
    def __init__(self, name , age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """告诉我有关我自己的细节"""
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    """代表每一位老师"""
    def __init__(self, name, age, salary):

        # 在这里你需要注意，当我们使用 SchoolMember 类的 tell 方法时，
        # 我们可以将 Teacher 或 Student 的实例看作 SchoolMember 的实例。
​        #同时，你会发现被调用的是子类型的 tell 方法，而不是 SchoolMember 的 tell 方法。
​        SchoolMember.__init__(self, name, age)
​        self.salary = salary
​        print('(Initialized Teacher: {})'.format(self.name))
    # 重载父类方法
​    def tell(self):
​        SchoolMember.tell(self)
​        print('Salary: "{:d}"'.format(self.salary))




class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    # 重载父类方法
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# 打印一行空白行
print()
members = [t,s]
for member in members:
    # 对全体师生工作
    member.tell()</code></pre>

输出：

<pre><code>(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"</code></pre>

**它是如何工作的**

要想使用继承，在定义类[^6]时我们需要在类后面跟一个包含基类名称的元组。然后，我们会注意到基类的 `__init__` 方法是通过 `self` 变量被显式调用的，因此我们可以初始化对象的基类部分。下面这一点很重要，需要牢记——因为我们在 `Teacher` 和 `Student` 子类中定义了 `__init__` 方法，Python 不会自动调用基类 `SchoolMember` 的构造函数，你必须自己显式地调用它。

相反，如果我们_没有_在一个子类中定义一个 `__init__` 方法，Python 将会自动调用基类的构造函数。

我们会观察到，我们可以通过在方法名前面加上基类名作为前缀，再传入 `self` 和其余变量，来调用基类的方法。

在这里你需要注意，当我们使用 `SchoolMember` 类的 `tell` 方法时，我们可以将 `Teacher` 或 `Student` 的实例看作 `SchoolMember` 的实例。

同时，你会发现被调用的是子类型的 `tell` 方法，而不是 `SchoolMember` 的 `tell` 方法。理解这一问题的一种思路是 Python *总会*从当前的实际类型中开始寻找方法，在本例中即是如此。如果它找不到对应的方法，它就会在该类所属的基本类中依顺序逐个寻找属于基本类的方法，这个基本类是在定义子类时后跟的元组指定的。

这里有一条有关术语的注释——如果继承元组（Inheritance Tuple）中有超过一个类，这种情况就会被称作**多重继承（Multiple Inheritance）**。

`end` 参数用在超类的 `tell()` 方法的 `print` 函数中，目的是打印一行并允许下一次打印在同一行继续。这是一个让 `print` 能够不在打印的末尾打印出 `\n` （新行换行符）符号的小窍门。

### 总结

我们已经探索了有关类和对象的各个方面，还有与它们相关的各类术语。我们还了解了面向对象编程的益处与陷阱。Python 是高度面向对象的，从长远来看，了解这些概念对你大有帮助。

接下来，我们将学习如何处理输入与输出，以及如何在 Python 中访问文件。

**更多请扫码关注**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>
