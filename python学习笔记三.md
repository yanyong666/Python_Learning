>微信公众号： 点击蓝色字体<font color=blue size=2.5>小白图像与视觉</font>进行关注
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言

# 下面主要讲函数
------------------------------
> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想

[TOC]

# 函数

函数（Functions）是指可重复使用的程序片段。它们允许你为某个代码块赋予名字，允许你通过这一特殊的名字在你的程序任何地方来运行代码块，并可重复任何次数。这就是所谓的*调用（Calling）*函数。我们已经使用过了许多内置的函数

函数可以通过关键字 `def` 来定义。这一关键字后跟一个函数的*标识符*名称，再跟一对圆括号，其中可以包括一些变量的名称，再以冒号结尾，结束这一行。随后而来的语句块是函数的一部分。下面的案例将会展示出这其实非常简单：

案例（保存为 `function1.py`）：

<pre><code class="lang-python">def say_hello():
    #  该块属于这一函数
    print('hello python')
# 函数结束
say_hello()  # 调用函数
say_hello()  # 再次调用
</code></pre>

输出：

<pre><code>hello python
hello python</code></pre>

要注意到我们可以两次调用相同的函数，这意味着我们不必重新把代码再写一次。

## 函数参数

函数可以获取参数，这个参数的值由你所提供。这些参数与变量类似，这些变量的值在我们调用函数时已被定义，且在函数运行时均已赋值完成。

函数中的参数通过将其放置在用以定义函数的一对圆括号中指定，并通过逗号予以分隔。当我们调用函数时，我们以同样的形式提供需要的值。要注意在此使用的术语——在定义函数时给定的名称称作_“形参”（Parameters）_，在调用函数时你所提供给函数的值称作_“实参”（Arguments）_。

案例（保存为 `function_param.py`）：

<pre><code class="lang-python">def print_max(a, b):
    if a > b:
        print(a, 'is maxinum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maxinum')
# 直接传递函数参数值
print_max(3,4)

x = 5
y =7
# 以参数的形式传递变量
print_max(x,y)
print(x, y) # 全局变量不受局部影响


def print_min(a, b):
    if a < b:
        print(a, 'is the min')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is the min')

# 直接传递实参
print_min(3,4)

# 以变量当做实数形式传递 #  print_max(x, y) 将使得实参 x 的值将被赋值给形参 a ，而实参 y 的值将被赋值给形参 b
x = 15
y = 17
print_min(x, y)
print(x, y)

</code></pre>

输出：

<pre><code>4 is maxinum
7 is maxinum
5 7
3 is the min
15 is the min
15 17</code></pre>

## 局部变量

当你在一个函数的定义中声明变量时，它们不会以任何方式与身处函数之外但具有相同名称的变量产生关系，也就是说，这些变量名只存在于函数这一*局部（Local）*。这被称为变量的*作用域（Scope）*。所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始。

案例（保存为 `function_local.py`）：

<pre><code class="lang-python">#W 主代码块中的 x 则不会受到影响
x = 50

def func(x):
    print('x is', x)
    x = 2  #  x 是我们这一函数块的局部变量
    print('changed local x to', x)

func(x)
print('x is still', x)
</code></pre>

输出：

<pre><code>x is 50
changed local x to 2
x is still 50</code></pre>

## `global` 语句 {#global-statement}

如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），那么你必须告诉 Python 这一变量并非局部的，而是*全局（Global）*的。我们需要通过 `global` 语句来完成这件事。因为在不使用 `global` 语句的情况下，不可能为一个定义于函数之外的变量赋值。

你可以使用定义于函数之外的变量的值（假设函数中没有具有相同名字的变量）。然而，这种方式不会受到鼓励而且应该避免，因为它对于程序的读者来说是含糊不清的，无法弄清楚变量的定义究竟在哪。而通过使用 `global` 语句便可清楚看出这一变量是在最外边的代码块中定义的。

案例（保存为 `function_global.py`）：

<pre><code class="lang-python">x = 55

def func():
    global x # 将 x 定义 成全局变量

    print('x is', x)
    x = 5
    print('changed global x to', x)

func()
print('value of x is', x)
</code></pre>

输出：

<pre><code>x is 55
changed global x to 5
value of x is 5</code></pre>
`global` 语句用以声明 `x` 是一个全局变量——因此，当我们在函数中为 `x` 进行赋值时，这一改动将影响到我们在主代码块中使用的 `x` 的值。

你可以在同一句 `global` 语句中指定不止一个的全局变量，例如 `global x, y, z`。


## 默认参数值 {#default-arguments}

对于一些函数来说，你可能为希望使一些参数*可选*并使用默认的值，以避免用户不想为他们提供值的情况。默认参数值可以有效帮助解决这一情况。你可以通过在函数定义时附加一个赋值运算符（`=`）来为参数指定默认参数值。

案例（保存为 `function_default.py`）：

<pre><code class="lang-python">def say(messages, times = 1):
    print(messages * times)

say('hello')
say('world', 5)
say('yy', 10)

</code></pre>

输出：

<pre><code>hello
worldworldworldworldworld
yyyyyyyyyyyyyyyyyyyy</code></pre>

名为 `say` 的函数用以按照给定的次数打印一串字符串。如果我们没有提供一个数值，则将按照默认设置，只打印一次字符串。我们通过为参数 `times` 指定默认参数值 `1` 来实现这一点。

在第一次使用 `say` 时，我们只提供字符串因而函数只会将这个字符串打印一次。在第二次使用 `say` 时，我们既提供了字符串，同时也提供了一个参数 `5`，声明我们希望*说（Say）*这个字符串五次。

> *注意*
> 
> 只有那些位于参数列表末尾的参数才能被赋予默认参数值，意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。
> 
> 这是因为值是按参数所处的位置依次分配的。举例来说，`def func(a, b=5)` 是有效的，但 `def func(a=5, b)` 是*无效的*。

## 关键字参数

如果你有一些具有许多参数的函数，而你又希望只对其中的一些进行指定，那么你可以通过命名它们来给这些参数赋值——这就是*关键字参数（Keyword Arguments）*——我们使用命名（关键字）而非位置（一直以来我们所使用的方式）来指定函数中的参数。

这样做有两大优点——其一，我们不再需要考虑参数的顺序，函数的使用将更加容易。其二，我们可以只对那些我们希望赋予的参数以赋值，只要其它的参数都具有默认参数值。

案例（保存为 `function_keyword.py`）：

<pre><code class="lang-python">def func(a, b=5 ,c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3,7)

# 关键字参数c指定了c=24
func(25,c=24)

# 关键字参数c指定了50 ，a指定了100 尽管a在c定义
func(c=50, a=100)</code></pre>

输出：

<pre><code>a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50</code></pre>

名为 `func` 的函数有一个没有默认参数值的参数，后跟两个各自带有默认参数值的参数。

在第一次调用函数时，`func(3, 7)`，参数 `a` 获得了值 `3`，参数 `b` 获得了值 `7`，而 `c` 获得了默认参数值 `10`。

在第二次调用函数时，`func(25, c=24)`，由于其所处的位置，变量 `a` 首先获得了值 25。然后，由于命名——即关键字参数——指定，变量 `c` 获得了值 `24`。变量 `b` 获得默认参数值 `5`。

在第三次调用函数时，`func(c=50, a=100)`，我们全部使用关键字参数来指定值。在这里要注意到，尽管 `a` 在 `c` 之前定义，但我们还是在变量 `a` 之前指定了变量 `c`。

## 可变参数

有时你可能想定义的函数里面能够有_任意_数量的变量，也就是参数数量是可变的，这可以通过使用星号来实现（将下方案例保存为 `function_varargs.py`）：

<pre><code class="lang-python">"""
1.当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数 （Positional Arguments）
都将被收集并汇集成一个称为“param”的元组（Tuple）。
类似地，
2.当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字
参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。

3.每一个函数都在其末尾隐含了一句 return None ，除非你写了你自己的 return 语句。
你可 以运行 print(some_function()) ，其中 some_function 函数不使用 return 语句，
就像这样：
        def some_function():
            pass
"""


def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
#   return None
print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
# 每一个函数都在其末尾隐含了一句 return None</code></pre>

输出：

<pre><code>a 10
single_item 1
single_item 2
single_item 3
Jack 1123
John 2231
Inge 1560
None</code></pre>

## `return` 语句 {#return-statement}

`return` 语句用于从函数中*返回*，也就是中断函数。我们也可以选择在中断函数时从函数中*返回一个值*。

案例（保存为 `function_return.py`）：

<pre><code class="lang-python">def maxinum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'the numbers are equal'
    else:
        return y


print(maxinum(3,4))

print(maxinum(5,6))


def mininum(a, b):
    if a < b:
        return a
    elif a == b:
        return 'a is equal b'
    else:
        return b

print(mininum(8,3))

</code></pre>

输出：

<pre><code>4
6
3</code></pre>

> 提示：有一个名为 `max` 的内置函数已经实现了“找到最大数”这一功能，所以尽可能地使用这一内置函数。

## DocStrings

Python 有一个甚是优美的功能称作*文档字符串（Documentation Strings）*，在称呼它时通常会使用另一个短一些的名字*docstrings*。DocStrings 是一款你应当使用的重要工具，它能够帮助你更好地记录程序并让其更加易于理解。令人惊叹的是，当程序实际运行时，我们甚至可以通过一个函数来获取文档！

案例（保存为 `function_docstring.py`）：

<pre><code class="lang-python">
def print_max(x, y):
    '''打印两个数值中的最大数值。

    这两个数应该是整数'''
    # 转换成整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is the max')
    elif x == y:
        print('x is equal to y')
    else:
        print(y, 'is the max')

print_max(5,6)
print(print_max.__doc__)
 %}</code></pre>

输出：

<pre><code>6 is the max
打印两个数值中的最大数值。

    这两个数应该是整数</code></pre>


## 总结

我们已经了解了许多方面的函数，但我们依旧还未覆盖到所有类型的函数。不过，我们已经覆盖到了大部分你每天日常使用都会使用到的 Python 函数。接下来，我们将了解如何创建并使用 Python 模块。


**更多请扫码关注**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>
