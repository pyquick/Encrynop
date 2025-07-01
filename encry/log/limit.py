import os,shutil,getpass
from encry.panic.panic import *
from .log import LogManager
class Limit_Size:
    super.__init__()
    #需要获取文件夹总大小,每一个文件大小.
    def __init__(self,folder_limit,file_limit):
        self.folder_limit=folder_limit
        self.file_limit=file_limit
        self.path=f"/Users/{getpass.getuser()}/.encry/log"
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
    def get_one_file_size(self,file_path):
        """计算单个文件的大小"""
        return os.path.getsize(file_path)
    def convert_size(size_bytes):
        """将字节转换为可读格式 (KB, MB, GB)"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    def limit_size_with_folder(self):
        #初级超过返回弹出警告,并报告warning panic
        self.limit_size_fo=self.convert_size(self.folder_limit)
        #去掉后面所有非数字字符
        try:
            self.limit_size_fo= float(str(self.limit_size_fo).rstrip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '))
        except ValueError:
            a=LogManager("limit(limit_size_with_folder)","ERROR")
            a.auto("limit_size_fo is not a number")
            raise Panic("limit_size_with_folder:limit_size_fo is not a number",2,"ValueError").raise_panic()
        