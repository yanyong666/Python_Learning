import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG, #10
        'info': logging.INFO, #20
        'warning': logging.WARNING,#30
        'error': logging.ERROR,#40
        'critical': logging.CRITICAL#50
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

log.logger.info('[显示log] hello, world')
log.logger.warning('[警告log] hello, world')