"""
pycharm 中自动补全代码提示符前的符号解释
p: parameter参数
m: method 方法
c: class 类
v: variable变量
f: fired字段或function函数

"""

import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test0.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test0.log')

print("Logging to", logging_file)
print(dir(logging))
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(filename)s : %(levelname)s : %(name)s :%(message)s',
    filename=logging_file,
    filemode='w',
    #datefmt='%Y-%m-%d %A %H:%M:%S',

)
logging.debug("start of the program")
logging.info("doing something")
logging.warning("dying now")
