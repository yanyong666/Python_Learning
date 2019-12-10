#Logger is also the first to filter the message based on a level —
# if you set the logger to INFO, and all handlers to DEBUG,
# you still won't receive DEBUG messages on handlers —
# they'll be rejected by the logger itself. If you set logger to DEBUG, but all handlers to INFO, you won't receive any DEBUG messages either —
# because while the logger says "ok, process this", the handlers reject it (DEBUG < INFO).
#验证
import logging

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

# 建立一个filehandler来把日志记录在文件里，级别为debug以上
fh = logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)

# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 将相应的handler添加在logger对象中
logger.addHandler(ch)
logger.addHandler(fh)

# 开始输出日志
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
