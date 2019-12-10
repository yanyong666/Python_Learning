# 使用logging打印日志到标准输出
"""
logger：产生日志的对象

Filter：过滤日志的对象

Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端

Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

"""

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

