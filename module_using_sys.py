"""
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


