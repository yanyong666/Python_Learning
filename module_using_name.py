"""
每个模块都有一个名称，而模块中的语句可以找到它们所处的模块的名称。
这对于确定模块 是独立运行的还是被导入进来运行的这一特定目的来说大为有用。
正如先前所提到的，当模 块第一次被导入时，它所包含的代码将被执行。
我们可以通过这一特性来使模块以不同的方式运行，
这取决于它是为自己所用还是从其它从的模块中导入而来。
这可以通过使用模块的 __name__ 属性来实现
"""

if __name__ == '__main__':
    print('this program is being run by itself')
else:
    print('I am being imported from another module')

