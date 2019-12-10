>微信公众号：**小白图像与视觉**
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言。
>
<font color=blus size=5>周五啦</font>

<img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573053527441&di=c2d5e893dd93a8cefef7ecf23426c07f&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn23%2F0%2Fw1200h1200%2F20180527%2F7b66-hcaquev1363380.jpg" width="300" hegiht="300" align=center/>

## 在 Windows 中安装

访问 https://www.python.org/downloads/ 并下载最新版本的 Python。在本书撰写的时点，最新版本为 Python 3.5.1。
其安装过程与其它 Windows 平台的软件的安装过程无异。

注意：请务必确认你勾选了 `Add Python 3.6 to PATH` 选项。

若要想改变安装位置，勾选 `Customize installation` 选项，点击 `Next` 后在安装位置中输入 `C:\python36` 。

如未勾选相关选项，你可以点击 `Add Python to environment variables` 。它和安装程序第一屏的 `Add Python 3.6 to PATH` 能起到相同效果。

你可以选择是否为所有用户安装启动器，这不会产生多大影响。启动器用以切换已安装的不同版本的 Python。

如果你的环境变量（Path）未正确设置，可以遵循上述步骤予以修正。否则，请参阅 `在 Windows 中运行 Python 提示符` 。

注意：对于那些对编程有所了解的人，如果你熟悉 Docker，可以参阅 [Python in Docker](https://hub.docker.com/_/python/) 和 [Docker on Windows](https://docs.docker.com/windows/)。

## 在 GNU/Linux 下安装

对于 GNU/Linux 用户，你可以使用发行版的包管理器来安装 Python 3，例如在 Debian 与 Ubuntu 平台下，你可以输入命令：`sudo apt-get update && sudo apt-get install python3` 。

要想验证安装是否成功，你可以通过打开 `Terminal` 应用或通过按下 `Alt + F2` 组合键并输入 `gnome-terminal` 来启动终端程序。如果这不起作用，请查阅你所使用的的 GNU/Linux 发行版的文档。现在，运行 `python3` 命令来确保其没有任何错误。

你会看到在运行命令后 Python 的版本信息显示在屏幕上：

<!-- 输出内容应与 book.json 中的 pythonVersion 变量相匹配-->
```
$ python3 -V
Python 3.6.9
```

附注：`$` 是 Shell 的提示符。根据你电脑所运行的操作系统的设置的不同，它也会有所不同，在之后的内容中我会使用 `$` 符号来代表提示符。

注意：输出的内容会因你的电脑而有所不同，其取决于你在你的电脑上安装的 Python 版本。
##python学习基础一之常量 字符串 转义字符 格式化
-----------------------------------------

```python
# 1.各种常量 字符串 转义字符 格式化 等等
# 格式化方法 python 索引从0开始 转换至字符串的工作将由 format 方法自 动完成
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('why id {0} playing with that python'.format(name))
# this is not a good idea 明确转换至字符串
print(name + ' is ' + str(age) +  ' years old')

# Python 中 format 方法所做的事情便是将每个参数值替换至格式所在的位置。这之中可以有 更详细的格式
# 对于浮点数 '0.333' 保留小数点后三位
print('{0:.3f}'.format(1.0/3))

# 使用下划线填充文本
# 使用（^）定义'__hello__'字符串长度11
print('{0:_^11}'.format('hello'))

# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte of Python'))

# print 总默认以一个不可见的新的一行字符（\n）结尾
print('a', end='')
print('b', end='')
print('')
# 转义序列（Escape Sequence）
# 转义序列 \\ 来指定反斜杠本身
# 新一行的转义序列—— \n
# 的转义序列是制表符： \t
print('what\'s your name')
print("what's your sex")
print(
'''这是一段多行字符串。这是它的第一行。 
This is the second line. 
"What's your name?," I asked.
 He said "Bond, James Bond." 
 ''')
print('this is the first line\nthis is the second line')
print('this is the first line\tthis is the second line')
print("this is the first sentence.\
 this is the second sentence") #放置在末尾的反斜杠表示字符串将在下一行继 续，但不会添加新的一行
# 输出原始未经过处理的字符串 比如转义字符\n 在前面加r或者R
print(r"Newlines are indicated by \n")
```

```bash
Swaroop was 20 years old when he wrote this book
why id Swaroop playing with that python
Swaroop is 20 years old
0.333
___hello___
Swaroop wrote A Byte of Python
ab
what's your name
what's your sex
这是一段多行字符串。这是它的第一行。 
This is the second line. 
"What's your name?," I asked.
 He said "Bond, James Bond." 
 
this is the first line
this is the second line
this is the first line	this is the second line
this is the first sentence. this is the second sentence
Newlines are indicated by \n
```


##python学习基础一之变量
-----------------------------------------
```python
# 2.变量
# 标识符命名
# 数据类型
# 对象 Python 是强（Strongly）面向对象的，因为所有的一切都是对象， 包括数字、字符串与 函数。

# 案例：使用变量与字面常量
i = 5
print(i)
i = i + 1
print(i)
# 变量只需被赋予某一值。不需要声明或定义数据类型
print('''This is a multi-line string.
this is the second line.''')
# 逻辑行与物理行  这三句等价  在python 最好不要使用;分号 可以用\代替多行输出
i = 5; print(i);
i = 5;
print(i);
i = 5; print(i)
s = 'This is a string. \
 This continues the string.'  # 显式行连接（Explicit Line Joining）
print(s)

'''
j = 5
# 下面将会发生错误 注意行首有一个空格 # 缩进错误：意外缩进
 print('value is', j)    # IndentationError: unexpected indent # 缩进错误：意外缩进
print('I repeat, the value is', j)
'''
```

```bash
This is a multi-line string.
this is the second line.
5
5
5
This is a string.  This continues the string.
```


**更多请参考**：
<center>![qrcode](https://note.youdao.com/yws/api/personal/file/WEB3e69e86739a238787b879f4789e6bff5?method=download&shareKey=bbdb8f100dfafe198e705daf0bdbfd1c)</center>