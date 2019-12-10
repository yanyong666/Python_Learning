>微信公众号： 点击蓝色字体<font color=blue size=2.5>小白图像与视觉</font>进行关注
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言

# 下面主要讲模块
------------------------------
> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想

[TOC]

### 模块

在上一章，你已经了解了如何在你的程序中通过定义一次函数工作来重用代码。那么如果你想在你所编写的别的程序中重用一些函数的话，应该怎么办？正如你可能想象到的那样，答案是模块（Modules）。

编写模块有很多种方法，其中最简单的一种便是创建一个包含函数与变量、以 `.py` 为后缀的文件。

另一种方法是使用撰写 Python 解释器本身的本地语言来编写模块。举例来说，你可以使用 [C 语言](http://docs.python.org/3/extending/)来撰写 Python 模块，并且在编译后，你可以通过标准 Python 解释器在你的 Python 代码中使用它们。

一个模块可以被其它程序*导入*并运用其功能。我们在使用 Python 标准库的功能时也同样如此。首先，我们要了解如何使用标准库模块。

案例 (保存为 `module_using_sys.py`):

<pre><code class="lang-python">"""
sys.argv 变量是一系列字符串的列表（List）（列表将在后面的章节予以详细解释）。
具体 而言， sys.argv 包含了命令行参数（Command Line Arguments）这一列表，
也就是使用命 令行传递给你的程序的参数。

"""
import os
import py_compile
import sys

print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nthe pythonpath is', sys.path, '\n')
print(os.getcwd())
# 中间文件路径
print(py_compile.compile('D:\PycharmProjects\module_using_sys.py'))

def exitfunc(value):
    print(value)
    sys.exit(0)
print('yanyong')
try:
    sys.exit(1)
except SystemExit as value:
    exitfunc('中途退出')
print('hello')


</code></pre>

输出：

<pre><code>the command line arguments are:
D:/PycharmProjects/module_using_sys.py


the pythonpath is ['D:\\PycharmProjects', 'D:\\PycharmProjects', 'D:\\JetBrains\\PyCharm 2019.1.3\\helpers\\pycharm_display', 'D:\\Anaconda3\\python36.zip', 'D:\\Anaconda3\\DLLs', 'D:\\Anaconda3\\lib', 'D:\\Anaconda3', 'D:\\Anaconda3\\lib\\site-packages', 'D:\\Anaconda3\\lib\\site-packages\\win32', 'D:\\Anaconda3\\lib\\site-packages\\win32\\lib', 'D:\\Anaconda3\\lib\\site-packages\\Pythonwin', 'D:\\JetBrains\\PyCharm 2019.1.3\\helpers\\pycharm_matplotlib_backend'] 

D:\PycharmProjects
D:\PycharmProjects\__pycache__\module_using_sys.cpython-36.pyc
yanyong
中途退出</code></pre>

**它是如何工作的**

首先，我们通过 `import` 语句*导入* `sys` 模块。基本上，这句代码将转化为我们告诉 Python 我们希望使用这一模块。`sys` 模块包含了与 Python 解释器及其环境相关的功能，也就是所谓的*系统*功能（*sys*tem）。

当 Python 运行 `import sys` 这一语句时，它会开始寻找 `sys` 模块。在这一案例中，由于其是一个内置模块，因此 Python 知道应该在哪里找到它。

如果它不是一个已编译好的模块，即用 Python 编写的模块，那么 Python 解释器将从它的 `sys.path` 变量所提供的目录中进行搜索。如果找到了对应模块，则该模块中的语句将在开始运行，并*能够*为你所使用。在这里需要注意的是，初始化工作只需在我们*第一次*导入模块时完成。

`sys` 模块中的 `argv` 变量通过使用点号予以指明，也就是 `sys.argv` 这样的形式。它清晰地表明了这一名称是 `sys` 模块的一部分。这一处理方式的另一个优点是这个名称不会与你程序中的其它任何一个 `argv` 变量冲突。

`sys.argv` 变量是一系列字符串的*列表（List）*（列表将在[后面的章节](./12.data_structures.md#data-structures)予以详细解释）。具体而言，`sys.argv` 包含了*命令行参数（Command Line Arguments）*这一列表，也就是使用命令行传递给你的程序的参数。

如果你正在使用一款 IDE 来编写并运行这些程序，请在程序菜单中寻找相关指定命令行参数的选项。

在这里，当我们运行 `python module_using_sys.py we are arguments` 时，我们通过 `python` 命令来运行 `module_using_sys.py` 模块，后面的内容则是传递给程序的参数。 Python 将命令行参数存储在 `sys.argv` 变量中供我们使用。

在这里要记住的是，运行的脚本名称在 `sys.argv` 的列表中总会位列第一。因此，在这一案例中我们将会有如下对应关系：`'module_using_sys.py'` 对应 `sys.argv[0]`，`'we'` 对应 `sys.argv[1]`，`'are'` 对应 `sys.argv[2]`，`'arguments'` 对应 `sys.argv[3]`。要注意到 Python 从 0 开始计数，而不是 1。

`sys.path` 内包含了导入模块的字典名称列表。你能观察到 `sys.path` 的第一段字符串是空的——这一空字符串代表当前目录也是 `sys.path` 的一部分，它与 `PYTHONPATH` 环境变量等同。这意味着你可以直接导入位于当前目录的模块。否则，你必须将你的模块放置在 `sys.path` 内所列出的目录中。

另外要注意的是当前目录指的是程序启动的目录。你可以通过运行 `import os; print(os.getcwd())` 来查看你的程序目前所处在的目录。

### 按字节码编译的 .pyc 文件 {#pyc}

导入一个模块是一件代价高昂的事情，因此 Python 引入了一些技巧使其能够更快速的完成。其中一种方式便是创建*按字节码编译的（Byte-Compiled）*文件，这一文件以 `.pyc` 为其扩展名，是将 Python 转换成中间形式的文件（还记得[《介绍》](./04.about_python.md#interpreted)一章中介绍的 Python 是如何工作的吗？）。这一 `.pyc` 文件在你下一次从其它不同的程序导入模块时非常有用——它将更加快速，因为导入模块时所需要的一部分处理工作已经完成了。同时，这些按字节码编译的文件是独立于运行平台的。

注意：这些 `.pyc` 文件通常会创建在与对应的 `.py` 文件所处的目录中。如果 Python 没有相应的权限对这一目录进行写入文件的操作，那么 `.pyc` 文件将_不会_被创建。

## `from..import` 语句 {#from-import-statement}

如果你希望直接将 `argv` 变量导入你的程序（为了避免每次都要输入 `sys.`），那么你可以通过使用 `from sys import argv` 语句来实现这一点。

> **警告：**一般来说，你应该尽量*避免*使用 `from...import` 语句，而去使用 `import` 语句。这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。

案例：

```python
# 案例1
from math import sqrt
print("square root of 16 is", sqrt(16))

# 案例2
"""
Ping发送一个ICMP(Internet Control Messages Protocol,因特网信报控制协议)；
回声请求消息给目的地并报告是否收到所希望的ICMPecho （ICMP回声应答）
例如：
    ping ip -n -r -w  (-n表示测试发送N个数据包 -r表示经过多少个路由 -w表示响应时间)  还可以有一堆参数
"""
import os
#import sys   这种方法导入sys模块，需使用sys.argv
from sys import argv  #这种方法导入sys模块，可直接使用argv
def ping(net,start=1,end=85,n=1,r=3,w=3):
    for i in range(start,end+1):
        ip=net+"."+str(i)
        command="ping %s -n %d -r %d -w %d"%(ip,n,r,w)
        print(ip,("通","不通")[os.system(command)])  #os.system(command)：运行command命令
if len(argv) not in [2,4,6]:
    print("参数输入错误！")
    print("运行示例：")
    print("from_import.py 121.194.14")
    print("from_import.py 121.194.14 80 90")
    print("from_import.py 121.194.14 80 90 3 1")
    print("语法：from_import.py net startip endip count routs timeout")
elif len(argv)==2:
    net=argv[1]
    ping(net)
elif len(argv)==4:
    net=argv[1]
    ping(net,start=int(argv[2]),end=int(argv[3]))
else:
    net=argv[1]
    ping(net,start=int(argv[2]),end=int(argv[3]),n=int(argv[4]),w=int(argv[5]))

```

输出：
```bash
square root of 16 is 4.0

正在 Ping 121.194.14.80 具有 32 字节的数据:
请求超时。

121.194.14.80 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 0，丢失 = 1 (100% 丢失)，
121.194.14.80 不通

正在 Ping 121.194.14.81 具有 32 字节的数据:
来自 121.194.14.81 的回复: 字节=32 时间=102ms TTL=245
    路由: 10.0.1.17 ->
           101.4.114.230 ->
           101.4.119.5

121.194.14.81 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 102ms，最长 = 102ms，平均 = 102ms
121.194.14.81 通

正在 Ping 121.194.14.82 具有 32 字节的数据:
来自 121.194.14.82 的回复: 字节=32 时间=235ms TTL=50
    路由: 10.0.1.17 ->
           58.19.110.198 ->
           58.19.109.250

121.194.14.82 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 235ms，最长 = 235ms，平均 = 235ms
121.194.14.82 通

正在 Ping 121.194.14.83 具有 32 字节的数据:
来自 121.194.14.83 的回复: 字节=32 时间=332ms TTL=50
    路由: 10.0.1.17 ->
           58.19.110.198 ->
           58.19.109.246

121.194.14.83 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 332ms，最长 = 332ms，平均 = 332ms
121.194.14.83 通

正在 Ping 121.194.14.84 具有 32 字节的数据:
来自 121.194.14.84 的回复: 字节=32 时间=78ms TTL=53
    路由: 10.0.1.17 ->
           101.4.114.230 ->
           101.4.119.5

121.194.14.84 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 78ms，最长 = 78ms，平均 = 78ms
121.194.14.84 通

正在 Ping 121.194.14.85 具有 32 字节的数据:
来自 121.194.14.85 的回复: 字节=32 时间=257ms TTL=50
    路由: 10.0.1.17 ->
           58.19.110.198 ->
           58.19.109.254

121.194.14.85 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 257ms，最长 = 257ms，平均 = 257ms
121.194.14.85 通

正在 Ping 121.194.14.86 具有 32 字节的数据:
请求超时。

121.194.14.86 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 0，丢失 = 1 (100% 丢失)，
121.194.14.86 不通

正在 Ping 121.194.14.87 具有 32 字节的数据:
请求超时。

121.194.14.87 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 0，丢失 = 1 (100% 丢失)，
121.194.14.87 不通

正在 Ping 121.194.14.88 具有 32 字节的数据:
来自 121.194.14.88 的回复: 字节=32 时间=264ms TTL=53
    路由: 10.0.1.17 ->
           101.4.114.230 ->
           101.4.119.5

121.194.14.88 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 264ms，最长 = 264ms，平均 = 264ms
121.194.14.88 通

正在 Ping 121.194.14.89 具有 32 字节的数据:
请求超时。

121.194.14.89 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 0，丢失 = 1 (100% 丢失)，
121.194.14.89 不通

正在 Ping 121.194.14.90 具有 32 字节的数据:
来自 121.194.14.90 的回复: 字节=32 时间=135ms TTL=53
    路由: 10.0.1.17 ->
           101.4.114.230 ->
           101.4.119.5

121.194.14.90 的 Ping 统计信息:
    数据包: 已发送 = 1，已接收 = 1，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 135ms，最长 = 135ms，平均 = 135ms
121.194.14.90 通

```


### 模块的 `__name__` {#module-name}

案例（保存为 `module_using_name.py`）：

<pre><code class="lang-python">"""
每个模块都有一个名称，而模块中的语句可以找到它们所处的模块的名称。
这对于确定模块 是独立运行的还是被导入进来运行的这一特定目的来说大为有用。
正如先前所提到的，当模 块第一次被导入时，它所包含的代码将被执行。
我们可以通过这一特性来使模块以不同的方 式运行，
这取决于它是为自己所用还是从其它从的模块中导入而来。
这可以通过使用模块的 __name__ 属性来实现
"""

if __name__ == '__main__':
    print('this program is being run by itself')
else:
    print('I am being imported from another module')

%}</code></pre>

输出：


<pre><code>this program is being run by itself</code></pre>

**它是如何工作的**

每一个 Python 模块都定义了它的 `__name__` 属性。如果它与 `__main__` 属性相同则代表这一模块是由用户独立运行的，因此我们便可以采取适当的行动。

### 编写你自己的模块

编写你自己的模块很简单，这其实就是你一直在做的事情！这是因为每一个 Python 程序同时也是一个模块。你只需要保证它以 `.py` 为扩展名即可。下面的案例会作出清晰的解释。

案例（保存为 `mymodule.py`）：

<pre><code class="lang-python">def say_hi():
    print('Hi, this is mymodule speaking.')

__version__ = '0.1'
</code></pre>

上方所呈现的就是一个简单的*模块*。正如你所看见的，与我们一般所使用的 Python 的程序相比其实并没有什么特殊的区别。我们接下来将看到如何在其它 Python 程序中使用这一模块。

要记住该模块应该放置于与其它我们即将导入这一模块的程序相同的目录下，或者是放置在 `sys.path` 所列出的其中一个目录下。

另一个模块（保存为 `mymodule_demo.py`）：

<pre><code class="lang-python">import mymodule
mymodule.say_hi()
print('version', mymodule.__version__)</code></pre>

输出：

<pre><code>Hi, this is mymodule speaking.
version 0.1}</code></pre>


下面是一个使用 `from...import` 语法的范本（保存为 `mymodule_demo2.py`）：

<pre><code class="lang-python">from mymodule import say_hi,__version__

say_hi()
print('version',__version__)</code></pre>

`mymodule_demo2.py` 所输出的内容与 `mymodule_demo.py` 所输出的内容是一样的。

在这里需要注意的是，如果导入到 mymodule 中的模块里已经存在了 `__version__` 这一名称，那将产生冲突。这可能是因为每个模块通常都会使用这一名称来声明它们各自的版本号。因此，我们大都推荐最好去使用 `import` 语句，尽管这会使你的程序变得稍微长一些。

你还可以使用：

```python
from mymodule import *
```

这将导入诸如 `say_hi` 等所有公共名称，但不会导入 `__version__` 名称，因为后者以双下划线开头。

> **警告：**要记住你应该避免使用 import * 这种形式，即 `from mymodule import * `。

<!-- -->

> 
> Python 的一大指导原则是“明了胜过晦涩”。你可以通过在 Python 中运行 `import this` 来了解更多内容。

### `dir` 函数 {#dir-function}

内置的 `dir()` 函数能够返回由对象所定义的名称列表。
如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。

该函数接受参数。
如果参数是模块名称，函数将返回这一指定模块的名称列表。
如果没有提供参数，函数将返回当前模块的名称列表。

案例：

```python
$ python
>>> import sys

# 给出 sys 模块中的属性名称
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# 此处只展示部分条目

# 给出当前模块的属性名称
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__','sys']

# 创建一个新的变量 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']

# 删除或移除一个名称
>>> del a

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

**它是如何工作的**

首先我们看到的是 `dir` 在被导入的 `sys` 模块上的用法。我们能够看见它所包含的一个巨大的属性列表。

随后，我们以不传递参数的形式使用 `dir` 函数。在默认情况下，它将返回当前模块的属性列表。要注意到被导入模块的列表也会是这一列表的一部分。

给了观察 `dir` 函数的操作，我们定义了一个新的变量 `a` 并为其赋予了一个值，然后在检查 `dir` 返回的结果，我们就能发现，同名列表中出现了一个新的值。我们通过 `del` 语句移除了一个变量或是属性，这一变化再次反映在 `dir` 函数所处的内容中。

关于 `del` 的一个小小提示——这一语句用于*删除*一个变量或名称，当这一语句运行后，在本例中即 `del a`，你便不再能访问变量 `a`——它将如同从未存在过一般。

要注意到 `dir()` 函数能对*任何*对象工作。例如运行 `dir(str)` 可以访问 `str`（String，字符串）类的属性。

同时，还有一个 [`vars()`](http://docs.python.org/3/library/functions.html#vars) 函数也可以返回给你这些值的属性，但只是可能，它并不能针对所有类都能正常工作。

### 包

现在，你必须开始遵守用以组织你的程序的层次结构。变量通常位于函数内部，函数与全局变量通常位于模块内部。如果你希望组织起这些模块的话，应该怎么办？这便是包（Packages）应当登场的时刻。

包是指一个包含模块与一个特殊的 `__init__.py` 文件的文件夹，后者向 Python 表明这一文件夹是特别的，因为其包含了 Python 模块。

让我们这样设想：你想创建一个名为“world”的包，其中还包含着 “asia”、“africa”等其它子包，同时这些子包都包含了诸如“india”、 “madagascar”等模块。

下面是你会构建出的文件夹的结构：

```
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py
```

包是一种能够方便地分层组织模块的方式。你将在 [标准库](./17.stdlib.md#stdlib) 中看到许多有关于此的实例。

### 总结

如同函数是程序中的可重用部分那般，模块是一种可重用的程序。包是用以组织模块的另一种层次结构。Python 所附带的标准库就是这样一组有关包与模块的例子。

我们已经了解了如何使用这些模块并创建你自己的模块。

接下来，我们将学习一些有趣的概念，它们被称作数据结构。

****


**更多请扫码关注**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>



