from termcolor import cprint
from colorama import init
init()
#NEW:
#Panic: (FROM ENCRY.PANIC.PANIC)
#SOURCE: xxx(func)
# XXXERROR: XXX
#THis Panic is very serious.
#Please report https://github.com/pyquick/pyquick/issues/ to report this panic.
class Panic(Exception):
    def __init__(self,name,log,level=int,type_panic=str):
        self.log =log
        self.name=name
        self.level =level
        self.type_panic =type_panic
        super().__init__(f"{type_panic}({level}): {log}")  # 关键修改：初始化BaseException

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
#NEW:
#Panic: (FROM ENCRY.PANIC.PANIC)
#LEVEL: 1-Warning,2-Error,3-Serious,4-Panic
#SOURCE: xxx(func)
# XXXERROR: XXX
#THis Panic is very serious.
#Please report https://github.com/pyquick/pyquick/issues/ to report this panic.
        #cprint(f'Panic:{self.type_panic}({level_lookup[self.level]})[{self.name}]' ,'red',)
        cprint("PANIC: (FROM ENCRY.PANIC.PANIC)",'red')
        cprint(f"LEVEL: {level_lookup[self.level]}",'red')
        cprint(f'SOURCE: {self.name}','red')
        contact=self.panic(self.log)
        cprint(f'{self.type_panic}:', 'red',None,["reverse","underline","blink"])
        for i in contact:
            cprint(i.strip(),'red',None,["reverse","underline","blink"])
            
        if self.level>=3:
            cprint("This Panic is very serious.\nPlease report https://github.com/pyquick/pyquick/issues/ to report this panic.".strip(),'red',None)
            exit(self.level)
        else:
            return None
