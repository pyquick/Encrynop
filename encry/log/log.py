import logging,getpass,os,multiprocessing
from encry.panic.panic import *
import os
if os.name == 'nt':  
    import colorama
    colorama.init()  
class ProcessNameFormatter(logging.Formatter):
    def format(self, record):
        record.process_name = multiprocessing.current_process().name
        return super().format(record)
class ColoredFormatter(logging.Formatter):
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
    
    def __init__(self,log_name,log_level=str):
        self.log_level = log_level 
        self.log_level_list=list(self.log_level)
        for self.i in range(len(self.log_level)):
            self.log_level_list[self.i]=self.log_level[self.i].upper()
        self.log_level=""
        for self.i in self.log_level_list:
            self.log_level+=self.i
        self.log_name = log_name
        if(log_level is None):
            raise Panic(f"Log_level must str,not None.",3,"LogManager").raise_panic()
        # 日志级别映射
        self.LEVELS = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(self.LEVELS[self.log_level])
            
        self.path=f"/Users/{getpass.getuser()}/.encry/log/encry_{log_level}.log"
        try:
            os.makedirs(os.path.dirname(self.path))
        except Exception:
            pass
        self.formatter = ProcessNameFormatter(
            '%(asctime)s - %(process_name)s - %(name)s  - %(levelname)s - %(message)s'   
        )
        self.file_handler = logging.FileHandler(self.path)
        if log_level!="info":
            self.file_handler.setLevel(self.LEVELS[self.log_level])
        self.file_formatter = self.formatter
        self.file_handler.setFormatter(self.file_formatter)
        # 创建控制台处理器
        self.console_formatter = ColoredFormatter(
            '%(asctime)s - %(process_name)s - %(name)s - %(message)s - %(levelname)s'
        )
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(self.LEVELS[self.log_level])
        self.console_handler.setFormatter(self.console_formatter)
        # 添加处理器
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
    def info(self, msg):
        if(self.log_level!="info" and self.log_level is not None):
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.info(msg)
    def warning(self, msg):
        if(self.log_level!="warning" and self.log_level is not None):
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.warning(msg)
    def error(self, msg):
        if(self.log_level!="error" and self.log_level is not None):
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.error(msg)
    def debug(self, msg):
        if(self.log_level!="debug" and self.log_level is not None):
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.debug(msg)
    def critical(self, msg):
        if(self.log_level!="critical"):
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.critical(msg)
    def auto(self, msg):
        if self.log_level is  None:
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        elif(self.log_level=="DEBUG".upper()):
            self.logger.debug(msg)
        elif(self.log_level=="info".upper()):
            self.logger.info(msg)
        elif(self.log_level=="warning".upper()):
            self.logger.warning(msg)
        elif(self.log_level=="error".upper()):
            self.logger.error(msg)
        elif(self.log_level=="critical".upper()):
            self.logger.critical(msg)
            self.logger.critical(msg)
        else:
            raise Panic(f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
    

    

