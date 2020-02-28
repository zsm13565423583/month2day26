import logging.handlers
import os

from config import BASE_PATH
class  GetLogger:
    __logger = None
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            #获取日志器
            cls.__logger =logging.getLogger()
            #设置日志器
            cls.__logger.setLevel(logging.INFO)
            #获取处理器----midnight
            log_path = BASE_PATH + os.sep + "log" + os.sep + "hmtt.log"
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=2,
                                                           backupCount=2,
                                                           encoding="utf-8")

            #获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            #处理器设置格式器
            th.setFormatter(fmt)
            #日志器添加处理器
            cls.__logger.addHandler(th)
        return cls.__logger