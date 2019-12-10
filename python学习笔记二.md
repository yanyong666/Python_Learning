>微信公众号：**小白图像与视觉**
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言。
>
<font color=blus size=5>人生并不是只有一种可能</font>

#1. 运算符与表达式 {#op-exp}

你所编写的大多数语句（逻辑行）都包含了_表达式（Expressions）_。一个表达式的简单例子便是 `2+3`。表达式可以拆分成运算符（Operators）与操作数（Operands）。

_运算符（Operators）_是进行某些操作，并且可以用诸如 `+` 等符号或特殊关键词加以表达的功能。运算符需要一些数据来进行操作，这些数据就被称作_操作数（Operands）_。在上面的例子中 `2` 和 `3` 就是操作数。

##2. 运算符

接下来我们将简要了解各类运算符及它们的用法。

要记得你可以随时在解释器中对给出的案例里的表达式进行求值。例如要想测试表达式 `2+3`，则可以使用交互式 Python 解释器提示符：

```python
>>> 2 + 3
5
>>> 3 * 5
15
>>>
```

下面是可用运算符的速览：

- `+`（加）
    - 两个对象相加。
    - `3+5` 则输出 `8`。`'a' + 'b'` 则输出 `'ab'`。

- `-`（减）
    - 从一个数中减去另一个数，如果第一个操作数不存在，则假定为零。
    - `-5.2` 将输出一个负数，`50 - 24` 输出 `26`。

- `*`（乘）
    - 给出两个数的乘积，或返回字符串重复指定次数后的结果。
    - `2 * 3` 输出 `6`。`'la' * 3` 输出 `'lalala'`。

- `**` （乘方）
    - 返回 x 的 y 次方。
    - `3 ** 4` 输出 `81` （即 `3 * 3 * 3 * 3`）。

- `/` （除）
    - x 除以 y
    - `13 / 3` 输出 `4.333333333333333`。

- `//` （整除）
    - x 除以 y 并对结果_向下_取整至最接近的整数。
    - `13 // 3` 输出 `4`。
    - `-13 // 3` 输出 `-5`。

- `%` （取模）
    - 返回除法运算后的余数。
    - `13 % 3` 输出 `1`。`-25.5 % 2.25` 输出 `1.5`。

- `<<` （左移）
    - 将数字的位向左移动指定的位数。（每个数字在内存中以二进制数表示，即 0 和1）
    - `2 << 2` 输出 `8`。 `2` 用二进制数表示为 `10`。
    - 向左移 2 位会得到 `1000` 这一结果，表示十进制中的 `8`。

- `>>` （右移）
    - 将数字的位向右移动指定的位数。
    - `11 >> 1` 输出 `5`。
    - `11` 在二进制中表示为 `1011`，右移一位后输出 `101` 这一结果，表示十进制中的 `5`。

- `&` （按位与）
    - 对数字进行按位与操作。[^1]
    - `5 & 3` 输出 `1`。

- `|` （按位或）
    - 对数字进行按位或操作。[^2]
    - `5 | 3` 输出 `7`。

- `^`（按位异或）
    - 对数字进行按位异或操作。[^3]
    - `5 ^ 3` 输出 `6`。

- `~` （按位取反）[^4]
    - x 的按位取反结果为 -(x+1)。
    - `~5` 输出 `-6`。有关本例的更多细节可以参阅：http://stackoverflow.com/a/11810203 。

- `<` （小于）
    - 返回 x 是否小于 y。所有的比较运算符返回的结果均为 `True` 或 `False`。请注意这些名称之中的大写字母。
    - `5 < 3` 输出 `False`，`3 < 6` 输出 `True`。
    - 比较可以任意组成组成链接：`3 < 5 < 7` 返回 `True`。

- `>` （大于）
    - 返回 x 是否大于 y。
    - `5 > 3` 返回 `True`。如果两个操作数均为数字，它们首先将会被转换至一种共同的类型。否则，它将总是返回 `False`。

- `<=` （小于等于）
    - 返回 x 是否小于或等于 y。
    - `x = 3; y = 6; x<=y` 返回 `True`。

- `>=` （大于等于）
    - 返回 x 是否大于或等于 y。
    - `x = 4; y = 3; x>=3` 返回 `True`。

- `==` （等于）
    - 比较两个对象是否相等。
    - `x = 2; y = 2; x == y` 返回 `True`。
    - `x = 'str'; y = 'stR'; x == y` 返回 `False`。
    - `x = 'str'; y = 'str'; x == y` 返回 `True`。

- `!=` （不等于）
    - 比较两个对象是否不相等。
    - `x = 2; y = 3; x != y` 返回 `True`。

- `not` （布尔“非”）[^5]
    - 如果 x 是 `True`，则返回 `False`。如果 x 是 `False`，则返回 `True`。
    - `x = True; not x` 返回 `False`。

- `and` （布尔“与”）[^6]
    - 如果 x 是 `False`，则 `x and y` 返回 `False`，否则返回 y 的计算值。
    - 当 x 是 `False` 时，`x = False; y = True; x and y` 将返回 `False`。在这一情境中，Python 将不会计算 y，因为它已经了解 and 表达式的左侧是 `False`，这意味着整个表达式都将是 `False` 而不会是别的值。这种情况被称作短路计算（Short-circuit Evaluation）。

- `or`（布尔“或”）[^7]
    - 如果 x 是 `True`，则返回 `True`，否则它将返回 y 的计算值。
    - `x = Ture; y = False; x or y` 将返回 `Ture`。在这里短路计算同样适用。

##3. 数值运算与赋值的快捷方式

一种比较常见的操作是对一个变量进行一项数学运算并将运算得出的结果返回给这个变量，因此对于这类运算通常有如下的快捷表达方式：

```python
a = 2
a = a * 3
```

同样也可写作：

```python
a = 2
a *= 3
```

要注意到 `变量 = 变量 运算 表达式` 会演变成 `变量 运算 = 表达式`。

##4. 求值顺序

如果你有一个诸如 `2 + 3 * 4` 的表达式，是优先完成加法还是优先完成乘法呢？我们的高中数学知识会告诉我们应该先完成乘法。这意味着乘法运算符的优先级要高于加法运算符。

下面将给出 Python 中从最低优先级（最少绑定）到最高优先级（最多绑定）的优先级表。这意味着，在给定的表达式中，Python 将优先计算表中位列于后的较高优先级的运算符与表达式。

为了保持完整，下表是从 [Python 参考手册](http://docs.python.org/3/reference/expressions.html#operator-precedence) 中引用而来。你最好使用圆括号操作符来对运算符与操作数进行分组，以更加明确地指定优先级。这也能使得程序更加可读。你可以阅读[改变运算顺序](#changing-order-of-evaluation)来了解更多的细节。

- `lambda`：Lambda 表达式
- `if - else` ：条件表达式
- `or`：布尔“或”
- `and`：布尔“与”
- `not x`：布尔“非”
- `in, not in, is, is not, <, <=, >, >=, !=, ==`：比较，包括成员资格测试（Membership Tests）和身份测试（Identity Tests）。
- `|`：按位或
- `^`：按位异或
- `&`：按位与
- `<<, >>`：移动
- `+, -`：加与减
- `*, /, //, %`：乘、除、整除、取余
- `+x, -x, ~x`：正、负、按位取反
- `**`：求幂
- `x[index], x[index:index], x(arguments...), x.attribute`：下标、切片、调用、属性引用
- `(expressions...), [expressions...], {key: value...}, {expressions...}`：表示绑定或元组、表示列表、表示字典、表示集合

我们还没有遇到的运算符将在后面的章节中加以解释。

在上表中位列同一行的运算符具有_相同优先级_。例如 `+` 和 `-` 就具有相同的优先级。

##5. 改变运算顺序 {#changing-order-of-evaluation}

为了使表达式更加易读，我们可以使用括号。举个例子，`2 + (3 * 4)` 自是要比 `2 + 3 * 4` 要更加容易理解，因为后者还要求你要了解运算符的优先级。和其它的一切一样，使用括号同样也要适度（而不要过度），同时亦应不要像 `(2 + (3 * 4))` 这般冗余。

使用括号还有一个额外的优点——它能帮助我们改变运算的顺序。同样举个例子，如果你希望在表达式中计算乘法之前应先计算加法，那么你可以将表达式写作 `(2 + 3) * 4`。

##6. 结合性

运算符通常由左至右结合。这意味着具有相同优先级的运算符将从左至右的方式依次进行求值。如 `2 + 3 + 4` 将会以 `(2 + 3) +4` 的形式加以计算。

##7. 表达式

案例（将其保存为 `expression.py`）：

```python
length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
```

输出：

```
$ python expression.py
Area is 10
Perimeter is 14
```


#8. 控制流 {#control-flow}

截止到现在，在我们所看过的程序中，总是有一系列语句从上到下精确排列，并交由 Python 忠实地执行。如果你想改变这一工作流程，应该怎么做？就像这样的情况：你需要程序作出一些决定，并依据不同的情况去完成不同的事情，例如依据每天时间的不同打印出 '早上好' 'Good Morning' 或 '晚上好' 'Good Evening'？

正如你可能已经猜测到的那番，这是通过控制流语句来实现的。在 Python 中有三种控制流语句——`if` `for` 和 `while`。

## `if` 语句

`if` 语句用以检查条件：*如果* 条件为真（True），我们将运行一块语句（称作 _if-block_ 或 _if 块_），*否则* 我们将运行另一块语句（称作 _else-block_ 或 _else 块_）。其中 *else* 从句是可选的。

案例（保存为 `if.py`）：
```
'''
if 语句用以检查条件：如果 条件为真（True），我们将运行一块语句（称作 if-block 或 if 块），
否则 我们将运行另一块语句（称作 else-block 或 else 块）。其中 else 从句是可选 的。
'''

# 设置变量
number = 23
# input() 函数来获取用户 的猜测数
guess = int(input('Enter an integer: '))   # int 将这个字符串转换成一个整数并将其储存在变量 guess 中

# if条件语句
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it. ')
    print('(but you do ont win any prizes!)')
    # 新块从这里结束
elif guess < number:
    # 另一代码块
    print('No,it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No,it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')
# 这最后一句将在
# if 语句执行完毕后执行

```


输出：

<pre><code>Enter an integer: 12
No,it is a little higher than that
Done</code></pre>


> **针对 C/C++ 程序员的提示**
> 
> Python 中不存在 `switch` 语句。你可以通过使用 `if..elif..else` 语句来实现同样的事情（在某些情况下，使用一部[字典](./12.data_structures.md#dictionary)能够更快速地完成）。

## `while` 语句

`while` 语句能够让你在条件为真的前提下重复执行某块语句。 `while` 语句是 *循环（Looping）* 语句的一种。`while` 语句同样可以拥有 `else` 子句作为可选选项。

案例（保存为 `while.py`）：

```
"""
while 语句能够让你在条件为真的前提下重复执行某块语句。
while 语句是 循环 （Looping） 语句的一种。
while 语句同样可以拥有 else 子句作为可选选项。
"""

# 设置变量
number = 23

running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将会导致while 终止
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
        # 如果 while 循环中存在一个 else 代码块，它将总是被执行， 除非你通过 break 语句来中断这一循环
    #   break
else:
    print('The while loop is over.')
print('Done')

```

输出：

<pre><code>Enter an integer : 21
No, it is a little higher than that.
Enter an integer : 56
No, it is a little lower than that.
Enter an integer : 23
Congratulations, you guessed it.
Congratulations, you guessed it.
The while loop is over.
Done</code></pre>


`True` 和 `False` 被称作布尔（Boolean）型，你可以将它们分别等价地视为 `1` 与 `0`。

> **针对 C/C++ 程序员的提示**
> 
> 你可以在 `while` 循环中使用 `else` 从句。


## `for` 循环

`for...in` 语句是另一种循环语句，其特点是会在一系列对象上进行*迭代（Iterates）*

案例（保存为 `for.py`）：

```
"""
for...in 语句是另一种循环语句，其特点是会在一系列对象上进行迭代（Iterates），意即 它会遍历序列中的每一个项目。
"""
for i in range(1,5):
    print(i)
else:
    print('the for loop is over')  #   else 部分是可选的。当循环中包含他时，它总会在 for 循环结束后开始执 行，除非程序遇到了 break 语句。
print(list(range(0, 5)))
print(list(range(1, 5)))
print(list(range(1, 5, 2)))
```

输出：

<pre><code>1
2
3
4
the for loop is over
[0, 1, 2, 3, 4]
[1, 2, 3, 4]
[1, 3]</code></pre>


> **针对 C/C++/Java/C# 程序员的提示**
> 
> Python 中的 `for` 循环和 C/C++ 中的 `for` 循环可以说是完全不同。C# 程序员会注意到 Python 中的 `for` 循环与 C# 中的 `foreach` 循环相似。Java 程序员则会注意到它同样与 Java 1.5 中的 `for (int i : IntArray)` 无甚区别。
> 
> 在 C/C++ 中，如果你希望编写 `for (int i = 0; i < 5; i++)`，那么在 Python 你只需要写下 `for i in range(0,5)`。正如你所看到的，Python 中的 `for` 循环将更加简单，更具表现力且更不容易出错。

## `break` 语句 {#break-statement}

`break` 语句用以*中断*（Break）循环语句，也就是中止循环语句的执行，即使循环条件没有变更为 `False`，或队列中的项目尚未完全迭代依旧如此。

有一点需要尤其注意，如果你 *中断* 了一个 `for` 或 `while` 循环，任何相应循环中的 `else` 块都将*不会*被执行。

案例（保存为 `break.py`）：

```
"""
break 语句用以中断（Break）循环语句，也就是中止循环语句的执行，即使循环条件没有 变更为 False ，
或队列中的项目尚未完全迭代依旧如此。
有一点需要尤其注意，如果你 中断 了一个 for 或 while 循环，任何相应循环中的 else 块都将不会被执行。
"""

while True:
    s = input('Enter something: ')
    if s == 'q':
        break
    print('Length of the string is', len(s))
print('Done')
```
输出：

<pre><code>Enter something: 1
Length of the string is 1
Enter something: 23
Length of the string is 2
Enter something: 3
Length of the string is 1
Enter something: q
Done</code></pre>

## `continue` 语句 {#continue-statement}

`continue` 语句用以告诉 Python 跳过当前循环块中的剩余语句，并*继续*该循环的下一次迭代。

案例（保存为 `continue.py`）：
```
"""
continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭 代。
"""
while True:
    s = input('Enter something: ')
    if s == 'q':
        break
    if len(s) < 3:
        print('too small')
        continue
        print('i am not done')
    print('Input is of sufficient length')

```

输出：

<pre><code>Enter something: 1
too small
Enter something: as
too small
Enter something: awe
Input is of sufficient length
Enter something: q</code></pre>

要注意 `continue` 语句同样能用于 `for` 循环。

##9. 总结

我们已经了解了三种控制流语句——`if`，`while` 和 `for` ——及其相关的 `break` 与 `continue` 语句是如何工作的。这些语句是 Python 中一些最常用的部分，因此，习惯去使用它们是必要的。

**更多请参考**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>





