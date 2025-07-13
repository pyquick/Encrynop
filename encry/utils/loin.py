import logging,getpass,os,multiprocessing
from encry.panic.panic import *
import os
#log阉割版
if os.name == 'nt':  
    import colorama
    colorama.init()  
class ProcessNameFormatter(logging.Formatter):
    def format(self, record):
        record.process_name = multiprocessing.current_process().name
        return super().format(record)
class ColoredFormatter(ProcessNameFormatter):
    """为不同日志级别添加颜色的格式化器"""
    COLOR_CODES = {
        'DEBUG': '\033[0;36m',  # 青色
        'INFO': '\033[0;32m',   # 绿色
        'WARNING': '\033[1;33m', # 黄色
        'ERROR': '\033[1;31m',   # 红色
        'CRITICAL': '\033[1;41m' # 红色背景
    }
    RESET_CODE = '\033[0m'

    def format(self, record):
        # 先调用父类方法格式化
        formatted_message = super().format(record)
        # 根据日志级别添加颜色
        color = self.COLOR_CODES.get(record.levelname, '')
        if color:
            return f"{color}{formatted_message}{self.RESET_CODE}"
        return formatted_message
class LogManager:
    def __init__(self,log_name,log_level="INFO",write_info=False):
        self.log_level = log_level.upper()#日志级别
        self.write_info=write_info#是否写入INFO级别日志
        self.log_name = log_name#日志名称(通常为函数)
        if(log_level is None or (log_level!="DEBUG" and log_level!="INFO" and log_level!="WARNING" and log_level!="ERROR" and log_level!="CRITICAL")):
            raise Panic("LogManager__init__",f"Log_level must str,not None.",3,"LogManager").raise_panic()
        # 日志级别映射
        self.LEVELS = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(self.LEVELS[self.log_level])
        if os.name == 'nt':  
            self.path = os.path.join(os.environ["APPDATA"],".encry","log")
        elif os.name == 'posix':
            self.path=f"/Users/{getpass.getuser()}/.encry/log/encry_{log_level}.log"
        else:
            self.path = f"/var/log/encry/log/encry_{log_level}.log"
        try:
            os.makedirs(os.path.dirname(self.path))
        except Exception:
            pass
        self.formatter = ProcessNameFormatter(
            '%(asctime)s - %(process_name)s - %(name)s  - %(levelname)s - %(message)s'   
        )
        if self.log_level!="INFO".upper() or write_info:
            self.file_handler = logging.FileHandler(self.path)
            self.file_handler.setLevel(self.LEVELS[self.log_level])
            self.file_formatter = self.formatter
            self.file_handler.setFormatter(self.file_formatter)
        # 创建控制台处理器
        self.console_formatter = ColoredFormatter(
            '%(asctime)s - %(process_name)s - %(name)s - %(message)s - %(levelname)s - powered by loin'
        )
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(self.LEVELS[self.log_level])
        self.console_handler.setFormatter(self.console_formatter)
        # 添加处理器
        if self.log_level!="INFO".upper() or write_info:
            self.logger.addHandler(self.file_handler)
        #self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
    def info(self, msg):
        if(self.log_level!="info".upper() and self.log_level is not None):
            raise Panic("info",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.info(msg)
    def warning(self, msg):
        if(self.log_level!="warning".upper() and self.log_level is not None):
            raise Panic("warning",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.warning(msg)
    def error(self, msg):
        if(self.log_level!="error".upper() and self.log_level is not None):
            raise Panic("error",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.error(msg)
    def debug(self, msg):
        if(self.log_level!="debug".upper() and self.log_level is not None):
            raise Panic("debug",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.debug(msg)
    def critical(self, msg):
        if(self.log_level!="critical".upper()):
            raise Panic("critical",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.critical(msg)