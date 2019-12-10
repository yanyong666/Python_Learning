>微信公众号： 点击蓝色字体<font color=blue size=2.5>小白图像与视觉</font>进行关注
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言

下面主要讲输入输出与异常处理
------------------------------
> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想

[TOC]

## 输入与输出 {#io}

有些时候你的程序会与用户产生交互。举个例子，你会希望获取用户的输入内容，并向用户打印出一些返回的结果。我们可以分别通过 `input()` 函数与 `print` 函数来实现这一需求。

对于输入，我们还可以使用 `str` （String，字符串）类的各种方法。例如，你可以使用 `rjust` 方法来获得一个右对齐到指定宽度的字符串。你可以查看 `help(str)` 来了解更多细节。


## 用户输入内容

将以下程序保存为 `io_input.py`：

<pre><code class="lang-python"># 回文 使用切片功能翻转文本
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text ==reverse(text)

something = input("enter text: ")
if is_palindrome(something)==1:
    print("yes, it is a palindrome")
else:
    print("no, it is not a palindrome")
"""

enter text: 121
yes, it is a palindrome
enter text: i am yy
no, it is not a palindrome

"""

</code></pre>

输出：

<pre><code>enter text: 121
yes, it is a palindrome
</code></pre>

**它是如何工作的**

我们使用切片功能翻转文本。我们已经了解了我们可以通过使用 `seq[a:b]` 来从位置 `a` 开始到位置 `b` 结束来[对序列进行切片](./12.data_structures.md#sequence) 。我们同样可以提供第三个参数来确定切片的_步长（Step）_。默认的步长为 `1`，它会返回一份连续的文本。如果给定一个负数步长，如 `-1`，将返回翻转过的文本。

`input()` 函数可以接受一个字符串作为参数，并将其展示给用户。尔后它将等待用户输入内容或敲击返回键。一旦用户输入了某些内容并敲下返回键，`input()` 函数将返回用户输入的文本。

我们获得文本并将其进行翻转。如果原文本与翻转后的文本相同，则判断这一文本是[回文](http://en.wiktionary.org/wiki/palindrome)。

### 作业练习

要想检查文本是否属于回文需要忽略其中的标点、空格与大小写。例如，“Rise to vote, sir.”是一段回文文本，但是我们现有的程序不会这么认为。你可以改进上面的程序以使它能够识别这段回文吗？
```python
import string
def reverse(text):
    return  text[::-1]

def is_palindrome(text):

    text = text.lower()
    text = text.replace(' ','')
    for char in string.punctuation:
        text = text.replace(char,'')
    return text == reverse(text)

def main():
    something = input('enter text:')
    if is_palindrome(something)==1:
        print("yes, {0} is a palindrome".format(something))
    else:
        print("no, {0} is not a palindrome".format(something))

if __name__ == '__main__':
    main()
else:
    print("io_string.py was imported")


```
输出：
```bash
enter text:a b, b,a
yes, a b, b,a is a palindrome
```

## 文件

你可以通过创建一个属于 `file` 类的对象并适当使用它的 `read`、`readline`、`write` 方法来打开或使用文件，并对它们进行读取或写入。读取或写入文件的能力取决于你指定以何种方式打开文件。最后，当你完成了文件，你可以调用 `close` 方法来告诉 Python 我们已经完成了对该文件的使用。

案例（保存为 `io_using_file.py`）：

<pre><code class="lang-python">poem = '''\
if you like to do something 
i will tell you the programing
    use python!
'''

# 打开文件以编辑
f = open('poem.txt', 'w')
# 向文件中写文本
f.write(poem)
# close file
f.close()

# 如果没有特别指定
# 默认阅读的方式打开
f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:# # Zero length indicates EOF
        break
    print(line,end='')
#close file
f.close()

</code></pre>

输出：

<pre><code>if you like to do something 
i will tell you the programing
    use python!</code></pre>

**它是如何工作的**

首先，我们使用内置的 `open` 函数并指定文件名以及我们所希望使用的打开模式来打开一个文件。打开模式可以是阅读模式（`'r'`），写入模式（`'w'`）和追加模式（`'a'`）。我们还可以选择是通过文本模式（`'t'`）还是二进制模式（`'b'`）来读取、写入或追加文本。实际上还有其它更多的模式可用，`help(open)` 会给你有关它们的更多细节。在默认情况下，`open()` 会将文件视作文本（**t**ext）文件，并以阅读（**r**ead）模式打开它。

在我们的案例中，我们首先采用写入模式打开文件并使用文件对象的 `write` 方法来写入文件，并在最后通过 `close` 关闭文件。

接下来，我们重新在阅读模式下打开同一个文件。我们不需要特别指定某种模式，因为“阅读文本文件”是默认的。我们在循环中使用 `readline` 方法来读取文件的每一行。这一方法将会一串完整的行，其中在行末尾还包含了换行符。当一个_空_字符串返回时，它表示我们已经到达了文件末尾，并且通过 `break` 退出循环。

最后，我们通过 `close` 关闭了文件。

现在，你可以检查 `poem.txt` 文件的内容来确认程序确实对该文件进行了写入与读取操作。

## Pickle

Python 提供了一个叫作 `Pickle` 的标准模块，通过它你可以将_任何_纯 Python 对象存储到一个文件中，并在稍后将其取回。这叫作*持久地（Persistently）*存储对象。

案例（保存为 `io_pickle.py`）：

<pre><code class="lang-python">"""
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

</code></pre>

输出：

<pre><code>['apple', 'mango', 'carrot']</code></pre>

**它是如何工作的**

要想将一个对象存储到一个文件中，我们首先需要通过 `open` 以写入（**w**rite）二进制（**b**inary）模式打开文件，然后调用 `pickle` 模块的 `dump` 函数。这一过程被称作_封装（Pickling）_。

接着，我们通过 `pickle` 模块的 `load` 函数接收返回的对象。这个过程被称作_拆封（Unpickling）_。

## Unicode

截止到现在，当我们编写或使用字符串、读取或写入某一文件时，我们用到的只是简单的英语字符。

> 注意：如果你正在使用 Python 2，我们又希望能够读写其它非英语语言，我们需要使用 `unicode` 类型，它全都以字母 `u` 开头，例如 `u"hello world"`。

```python
>>> "hello world"
'hello world'
>>> type("hello world")
<class 'str'>
>>> u"hello world"
'hello world'
>>> type(u"hello world")
<class 'str'>
```

当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们的 Unicode 字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”。我们可以在这一格式下进行读取与写入，只需使用一个简单的关键字参数到我们的标准 `open` 函数中：

<pre><code class="lang-python"># modname.itemname
import io
f = io.open('abc.txt','wt', encoding = "utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding = "utf-8").read()
print(text)</code></pre>
输出：

<pre><code>Imagine non-English language here</code></pre>

**它是如何工作的**

现在你可以忽略 `import` 语句，我们会在[模块章节](./11.modules.md#modules)章节探讨有关它的更多细节。

每当我们诸如上面那番使用 Unicode 字面量编写一款程序时，我们必须确保 Python 程序已经被告知我们使用的是 UTF-8，因此我们必须将 `# encoding=utf-8` 这一注释放置在我们程序的顶端。[^4]

我们使用 `io.open` 并提供了“编码（Encoding）”与“解码（Decoding）”参数来告诉 Python 我们正在使用 Unicode。

你可以阅读以下文章来了解有关这一话题的更多内容：

- ["The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets"](http://www.joelonsoftware.com/articles/Unicode.html)
- [Python Unicode Howto](http://docs.python.org/3/howto/unicode.html)
- [Pragmatic Unicode talk by Nat Batchelder](http://nedbatchelder.com/text/unipain.html)

## 总结

我们已经讨论了有关输入和输出的多种类型，这些内容有关文件处理，有关 pickle 模块还有关于 Unicode。

接下来，我们将探索一些异常的概念。

## 异常概念

当你的程序出现例外情况时就会发生异常（Exception）。例如，当你想要读取一个文件时，而那个文件却不存在，怎么办？又或者你在程序执行时不小心把它删除了，怎么办？这些通过使用**异常**来进行处理。

类似地，如果你的程序中出现了一些无效的语句该怎么办？Python 将会对此进行处理，**举起（Raises）**它的小手来告诉你哪里出现了一个**错误（Error）**。

## 错误

你可以想象一个简单的 `print` 函数调用。如果我们把 `print` 误拼成 `Print` 会怎样？你会注意到它的首字母是大写。在这一例子中，Python 会_抛出（Raise）_一个语法错误。

```python
>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World
```

你会注意到一个 `NameError` 错误被抛出，同时 Python 还会打印出检测到的错误发生的位置。这就是一个错误**错误处理器（Error Handler）**[^2] 为这个错误所做的事情。

## 异常

我们将**尝试（Try）**去读取用户的输入内容。按下 `[ctrl-d]` 来看看会发生什么事情。

```python
>>> s = input('Enter something --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

此处 Python 指出了一个称作 `EOFError` 的错误，代表着它发现了一个*文件结尾（End of File）*符号（由 `ctrl-d` 实现）在不该出现的时候出现了。

## 处理异常

我们可以通过使用 `try..except` 来处理异常状况。一般来说我们会把通常的语句放在 try 代码块中，将我们的错误处理器代码放置在 except 代码块中。

案例（保存文 `exceptions_handle.py`）：

<pre><code class="lang-python">"""
处理一组异常可以这样写（其中e代表异常的实例）：
    import sys
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = a / b
        print("您输入的两个数相除的结果是：", c )
    except (IndexError, ValueError, ArithmeticError):
        print("程序发生了数组越界、数字格式异常、算术异常之一")
    except:
        print("未知异常")
"""
# coding=utf-8


a = 10
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(e.args)
print("done")</code></pre>

输出：

<pre><code>('division by zero',)
done</code></pre>

**它是如何工作的**

我们将所有可能引发异常或错误的语句放在 `try` 代码块中，并将相应的错误或异常的处理器（Handler）放在 `except` 子句或代码块中。`except` 子句可以处理某种特定的错误或异常，或者是一个在括号中列出的错误或异常。如果没有提供错误或异常的名称，它将处理_所有_错误与异常。

要注意到必须至少有一句 `except` 字句与每一句 `try` 字句相关联。不然，有一个 try 代码块又有什么意义？

如果没有任何错误或异常被处理，那么将调用 Python 默认处理器，它只会终端程序执行并打印出错误信息。我们已经在前面的章节里见过了这种处理方式。

你还可以拥有一个 `else` 子句与 `try..except` 代码块相关联。`else` 子句将在没有发生异常的时候执行。

在下一个案例中，我们还将了解如何获取异常对象以便我们可以检索其他信息。

## 抛出异常

你可以通过 `raise` 语句来_引发_一次异常，具体方法是提供错误名或异常名以及要_抛出（Thrown）_异常的对象。

你能够引发的错误或异常必须是直接或间接从属于 `Exception`（异常） 类的派生类。

案例（保存为 `exceptions_raise.py`）：

<pre><code class="lang-python"># ecoding=UTF-8

# 我们创建了我们自己的异常类型。这一新的异常类型叫作ShortInputException
class ShortInputException(Exception):
    '''一个有用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('enter something -->')
    if(len(text)) < 3:
        # raise 语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出 （Thrown）异常的对象
        raise ShortInputException(len(text),3)
    #其他工作在此正常执行
except EOFError:
    print('why did you do an EOF on me?')
except ShortInputException as e:
    print(('ShortInputException: The input was ' + '{0} long,expected at least {1}').format(e.length, e.atleast))
else:
    print('No exception was raised.')
</code></pre>

输出：

<pre><code>enter something -->a
ShortInputException: The input was 1 long,expected at least 3</code></pre>

**它是如何工作的**

在本例中，我们创建了我们自己的异常类型。这一新的异常类型叫作 `ShortInputException`。它包含两个字段——获取给定输入文本长度的 `length`，程序期望的最小长度 `atleast`。

在 `except` 子句中，我们提及了错误类，将该类存储 `as（为）` 相应的错误名或异常名。这类似于函数调用中的形参与实参。在这个特殊的 `except` 子句中我们使用异常对象的 `length` 与 `atleast` 字段来向用户打印一条合适的信息。

## Try ... Finally {#try-finally}

假设你正在你的读取中读取一份文件。你应该如何确保文件对象被正确关闭，无论是否会发生异常？这可以通过 `finally` 块来完成。

保存该程序为 `exceptions_finally.py`：

<pre><code class="lang-python">import sys
import time
f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
            print(line, end='')
            sys.stdout.flush()
            print("Press ctrl+c now")
            # 为了确保它能运行一段时间
            time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
        print("(Cleaning up: Closed the file)")</code></pre>



**它是如何工作的**

我们按照通常文件读取进行操作，但是我们同时通过使用 `time.sleep` 函数任意在每打印一行后插入两秒休眠，使得程序运行变得缓慢（在通常情况下 Python 运行得非常快速）。当程序在处在运行过过程中时，按下 `ctrl + c` 来中断或取消程序。

你会注意到 `KeyboardInterrupt` 异常被抛出，尔后程序退出。不过，在程序退出之前，finally 子句得到执行，文件对象总会被关闭。

另外要注意到我们在 `print` 之后使用了 `sys.stout.flush()`，以便它能被立即打印到屏幕上。

## 总结

我们已经讨论了 `try..except` 和 `try..finally` 语句的用法。同时我们也已经看到了如何创建我们自己的异常类型，还有如何抛出异常。

接下来，我们将探索 Python 的标准库。

**更多请扫码关注**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>




