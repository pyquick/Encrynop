from encry.panic.panic import *
from .log import *
from .limit import *
import threading
a=threading.Thread(target=Limit_Size(136314880,36700160).limit_size())
a.start()
a.join()
def loinf():
    try:
        info=LogManager("__INIT____INFO","INFO")
        info.info("THIS IS INFO/info")
        info.auto("THIS IS INFO/auto")
        return 0
    except:
        return 1
def loerr():
    try:
        err=LogManager("__INIT____ERR","ERROR")
        err.auto("THIS IS ERROR/auto")
        err.error("THIS IS ERROR/error")
        return 0
    except:
        return 1
def lode():
    try:
        de=LogManager("__INIT____DEBUG","DEBUG")
        de.debug("THIS IS DEBUG/debug")
        de.auto("THIS IS DEBUG/auto")
        return 0
    except:
        return 1
def lowar():
    try:
        war=LogManager("__INIT____WARN","WARNING")
        war.warning("THIS IS WARNING/warning")
        war.auto("THIS IS WARNING/auto")
        return 0
    except:
        return 1
def loal():
    try:
        cr=LogManager("__INIT____CRITICAL","CRITICAL")
        cr.critical("THIS IS CRITICAL/critical")
        cr.auto("THIS IS CRITICAL/auto")
        return 0
    except:
        return 1
def bug_re():
    
    result=[loinf(),lowar(),loerr(),lode(),loal()]
    for i in result:
        if i==1:
            raise Panic("__INIT__ bug_re","SOME PROBLEMS",4,"UNKNOWN").raise_panic()
        else:
            pass
    return None
bug_re()
    
