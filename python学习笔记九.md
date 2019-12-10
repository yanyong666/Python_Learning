>微信公众号： 点击蓝色字体<font color=blue size=2.5>小白图像与视觉</font>进行关注
>
>关于技术、关注`yysilence00`。有问题或建议，请公众号留言

下面主要讲标准库之`日志`logging
------------------------------
> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想

[TOC]

```
日志级别:
- CRITICAL 50
- ERROR 40
- WARNING 30
- INFO 20
- DEBUG 10

logging.basicConfig()函数中的具体参数含义

- filename：指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中；
- filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“w”还可指定为“a”；
- format：指定handler使用的日志显示格式；
- datefmt：指定日期时间格式。，格式参考strftime时间格式化（下文）
- level：设置rootlogger的日志级别
- stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数用到的格式化信息

- 参数	描述
- %(name)s	Logger的名字
- %(levelno)s	数字形式的日志级别
- %(levelname)s	文本形式的日志级别
- %(pathname)s	调用日志输出函数的模块的完整路径名，可能没有
- %(filename)s	调用日志输出函数的模块的文件名
- %(module)s	调用日志输出函数的模块名
- %(funcName)s	调用日志输出函数的函数名
- %(lineno)d	调用日志输出函数的语句所在的代码行
- %(created)f	当前时间，用UNIX标准的表示时间的浮 点数表示
- %(relativeCreated)d	输出日志信息时的，自Logger创建以 来的毫秒数
- %(asctime)s	字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
- %(thread)d	线程ID。可能没有
- %(threadName)s	线程名。可能没有
- %(process)d	进程ID。可能没有
- %(message)s	用户输出的消息

```

#1.先看一个简单的例子
使用logging打印日志到标准输出

```py
import logging
logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so') # will not print anything
```
输出：
> WARNING: root :Watch out!


#2.再看另外一个例子 

```python
"""
pycharm 中自动补全代码提示符前的符号解释
p: parameter参数
m: method 方法
c: class 类
v: variable变量
f: fired字段orfunction函数

"""
"""
pycharm 中自动补全代码提示符前的符号解释
p: parameter参数
m: method 方法
c: class 类
v: variable变量
f: fired字段orfunction函数

日志级别:
 最高   CRITICAL 50
        ERROR 40
        WARNING 30
        INFO 20
 最低   DEBUG 10

"""
import logging

#print(dir(logging))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(module)s - %(filename)s - %(levelname)s : %(message)s',
    #datefmt='%Y-%m-%d %A %H:%M:%S',

)
# logging 是一个模块 它调用自己的函数getLogger()返回给实例变量(即对象)
logger = logging.getLogger(__name__)
# logger是实例变量（即对象）调用自己的方法Method()   info()等等
logger.info("start print log")
logger.debug("do something")
logger.warning("Something maybe fail.")
logger.info("Finish")


```
```
2019-12-08 20:49:42,800 - logging_test - logging_test.py - INFO : start print log
2019-12-08 20:49:42,801 - logging_test - logging_test.py - WARNING : Something maybe fail.
2019-12-08 20:49:42,801 - logging_test - logging_test.py - INFO : Finish
```

上面两个案例说明python默认输出的最高级别是warning

#3.使用logging.baseConfig()将日志输入到文件

```py
# 使用logging打印日志到标准输出
"""
logger：产生日志的对象

Filter：过滤日志的对象

Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端

Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

"""
import os
import logging

logging.debug('调试debug')  # DEBUG = 10
logging.info('消息info')  # INFO = 20
logging.warning('警告warn')  # WARNING = 30
logging.error('错误error')  # ERROR = 40
logging.critical('严重critical')  # CRITICAL = 50

'''
WARNING:root:警告warn
ERROR:root:错误error
CRITICAL:root:严重critical
'''
logging.basicConfig(
    filename=os.path.join(os.getcwd(),'test2.log'),
    level=logging.DEBUG,
    format='%(asctime)s  %(filename)s : %(name)s : %(levelname)s  %(message)s',  # 定义输出log的格式
    filemode='a',
    datefmt='%Y-%m-%d %A %H:%M:%S',
)
logging.debug('this is a message')
```
在test2.log文件中输出下面内容
```
2019-12-07 Saturday 12:04:13  stalid_logging_1.py : DEBUG  this is a message
```
#4.logging 4种常用对象
- logger：产生日志的对象
- Filter：过滤日志的对象
- Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端
- Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

```py
import logging

logger=logging.getLogger()
# 创建一个handler 用于写入日志
fh = logging.FileHandler('test4.log', encoding='utf-8')

# 在创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
#logger对象可以添加多个fh和ch对象
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
```
在文件test4.log输出
```sh
2019-12-08 20:59:59,177 - root - WARNING - logger warning message
2019-12-08 20:59:59,178 - root - ERROR - logger error message
2019-12-08 20:59:59,178 - root - CRITICAL - logger critical message

```

#5.设置按照日志文件大小自动分割日志写入文件

```py
import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别

        # 向控制台输出日志
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)

        # 日志按文件大小写入文件
        # 1MB = 1024 * 1024 bytes
        # 这里设置文件的大小为500MB
        rotating_file_handler = handlers.RotatingFileHandler(
            filename=filename, mode='a', maxBytes=1024 * 1024 * 500, backupCount=5, encoding='utf-8')
        rotating_file_handler.setFormatter(format_str)
        self.logger.addHandler(rotating_file_handler)


log = Logger('all.log', level='info')

log.logger.info('[测试log] hello, world')
```

#6.按照间隔日期自动生成日志文件
```
import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别

        # 往文件里写入
        # 指定间隔时间自动生成文件的处理器
        timed_rotating_file_handler = handlers.TimedRotatingFileHandler(
            filename=filename, when=when, backupCount=backCount, encoding='utf-8')

        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        timed_rotating_file_handler.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(timed_rotating_file_handler)

        # 往屏幕上输出
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)


log = Logger('all.log', level='info')
log.logger.info('[测试log] hello, world')

```
#7.Logger的继承（了解）
```
import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S %p', )

ch = logging.StreamHandler()
ch.setFormatter(formatter)

logger1 = logging.getLogger('root')
logger2 = logging.getLogger('root.child1')
logger3 = logging.getLogger('root.child1.child2')

logger1.addHandler(ch)
logger2.addHandler(ch)
logger3.addHandler(ch)
logger1.setLevel(10)
logger2.setLevel(10)
logger3.setLevel(10)

logger1.debug('log1 debug')
logger2.debug('log2 debug')
logger3.debug('log3 debug')
```
输出
```
2019-12-08 21:06:55 PM - root - DEBUG -stalib_logging_4:  log1 debug
2019-12-08 21:06:55 PM - root.child1 - DEBUG -stalib_logging_4:  log2 debug
2019-12-08 21:06:55 PM - root.child1 - DEBUG -stalib_logging_4:  log2 debug
2019-12-08 21:06:55 PM - root.child1.child2 - DEBUG -stalib_logging_4:  log3 debug
2019-12-08 21:06:55 PM - root.child1.child2 - DEBUG -stalib_logging_4:  log3 debug
2019-12-08 21:06:55 PM - root.child1.child2 - DEBUG -stalib_logging_4:  log3 debug
```

**更多请扫码关注**：
<center>
<img src="https://note.youdao.com/yws/api/personal/file/WEB4c5a2ba9b0d3fcdf7fa67543141b1cc0?method=download&shareKey=d962d52c470d4121f8d0c474be34c56f" width="350" hegiht="350" align=center/>
</center>

