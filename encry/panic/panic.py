from termcolor import cprint
from colorama import init
from encry.log.log import *
init()
class Panic(BaseException):
    def __init__(self,log,level=int,type_panic=str):
        self.log =log
        self.level =level
        self.type_panic =type_panic
    def panic(self,log):
        logl=log.split('\n')
        return logl
    def raise_panic(self):
        level_lookup={
            1:'Warning',
            2:'Error',
            3:'Serious',
            4:'Panic',
        }
        cprint(f'Panic:{self.type_panic}({level_lookup[self.level]})' ,'red',)
        contact=self.panic(self.log)
        for i in contact:
            cprint(i.strip(),'red',None,["reverse","underline","blink"])
        if self.level>=3:
            cprint("This Panic is very serious.\nPlease report https://github.com/pyquick/pyquick/issues/ to report this panic.".strip(),'red',None)

            exit(self.level)
