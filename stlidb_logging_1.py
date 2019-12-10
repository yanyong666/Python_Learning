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
logging.error('错误error')  # ERR OR = 40
logging.critical('严重critical')  # CRITICAL = 50


logging.basicConfig(
    filename=os.path.join(os.getcwd(),'test2.log'),
    level=logging.DEBUG,
    format='%(asctime)s  %(filename)s : %(name)s : %(levelname)s  %(message)s',  # 定义输出log的格式
    filemode='a',
    datefmt='%Y-%m-%d %A %H:%M:%S',
)
logging.debug('this is a message')