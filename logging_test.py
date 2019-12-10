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
