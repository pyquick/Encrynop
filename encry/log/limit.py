import os,shutil,getpass
from traceback import format_list
from encry.panic.panic import *
from .log import LogManager
import threading,sys
class Limit_Size:
    def __init__(self,folder_limit=int,file_limit=int):
        self.folder_limit=folder_limit
        self.file_limit=file_limit
        self.path=f"/Users/{getpass.getuser()}/.encry/log"
        if(self.folder_limit<0 or self.file_limit<0 or self.folder_limit<self.file_limit):
            raise Panic("Limit_Size %(func)s"% {"func":sys._getframe().f_code.co_name},"Invalid Data",4,"DLE").raise_panic()
    def get_folder_size(self):
        """计算文件夹总大小（包括所有子文件）"""
        self.total_size = 0
        for self.dirpath, self.dirnames, self.filenames in os.walk(self.path):
            for self.f in self.filenames:
                self.fp = os.path.join(self.dirpath, self.f)
                # 跳过符号链接
                if not os.path.islink(self.fp):
                    self.total_size += os.path.getsize(self.fp)
        return self.total_size
    def get_all_file_size(self):
        """计算文件夹总大小（包括所有子文件）"""
        self.total_size = []
        for self.dirpath, self.dirnames, self.filenames in os.walk(self.path):
            for self.f in self.filenames:
                self.fp = os.path.join(self.dirpath, self.f)
                # 跳过符号链接
                if not os.path.islink(self.fp):
                    self.total_size .append( os.path.getsize(self.fp))
        return self.total_size
    def get_one_file_size(self,file_path):
        return os.path.getsize(file_path)
    def convert_size(self,size_bytes):
        """将字节转换为可读格式 (KB, MB, GB)"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    def to_bytes(self,value, unit):
        units = {
            'B': 1,
            'KB': 1024,
            'MB': 1024**2,
            'GB': 1024**3,
            'TB': 1024**4,
            'PB': 1024**5,
            'EB': 1024**6,
            'ZB': 1024**7,
            'YB': 1024**8
        }
        unit = unit.upper()  # 处理大小写不敏感
        if unit not in units:
            raise Panic("to_bytes","incorrunt unit.",4,"typeerror").raise_panic()
        return value * units[unit]
    #写一个函数,可以获取一个文件夹所有文件名,并返回一个列表
    def get_all_file_name(self) -> list:
        """获取文件夹所有文件名和大小，按文件大小降序返回"""
        self.file_name_list: list[tuple[str, int]] = []
        for self.dirpath, self.dirnames, self.filenames in os.walk(self.path):
            for self.f in self.filenames:
                self.fp = os.path.join(self.dirpath, self.f)
                # 跳过符号链接
                if not os.path.islink(self.fp):
                    file_size = os.path.getsize(self.fp)
                    self.file_name_list.append((self.f, file_size))
                    
        # 按文件大小降序排序
        self.file_name_list.sort(key=lambda x: x[1], reverse=True)
        self.result = []
        for i in self.file_name_list:
            self.result.append(i[0])
        try:
            self.result.remove("Thumbs.db")
        except:
            pass
        try:
            self.result.remove(".DS_Store")
        except:
            pass
        return self.result
        
    def limit_size(self):
        #初级超过返回弹出警告,并报告warning panic
        self.log_folder_size=self.get_folder_size()
        self.warn=LogManager("Limit_Size","WARNING")
        self.debug=LogManager("Delete_Size","DEBUG")
        self.file_names=self.get_all_file_name()
        self.file_size=self.get_all_file_size()
        list.sort(self.file_size,reverse=True)
        self.total=0
        self.mirror=self.file_names
        for i in range(len(self.file_names)):
            if(self.file_size[i]>self.file_limit):
                os.remove(os.path.join(self.path,self.file_names[i]))
                self.debug.debug(f"Deleted {self.file_names[i]}.")
        self.file_names=self.get_all_file_name()
        if self.log_folder_size<self.folder_limit:
            self.debug.auto("Great! Log folder size is under limit.")
            return
        if self.log_folder_size>self.log_folder_size and abs(self.log_folder_size-self.log_folder_size)<10000:
            self.warn.warning(f"Log folder out of limit.\nPlease check some logs.Size:{self.convert_size(self.get_folder_size())}")
            Panic("limit_size_with_folder","Log folder out of limit.\nPlease check some logs.",2,"FLE").raise_panic()
        elif self.log_folder_size>self.log_folder_size and abs(self.log_folder_size-self.log_folder_size)>10000:
            #删除由大到小的文件
            for i in self.file_size:
                self.total+=i
            for i in range(len(self.file_names)):
                self.debug.debug(f"DEL Files:{self.file_names[i]}")
                os.remove(os.path.join(self.path,self.file_names[i]))
                self.total-=self.file_size[i]
                if(self.total<self.folder_limit and self.file_size[i]<self.file_limit):
                    break
        
                
            

        

            
        