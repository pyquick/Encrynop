from encry.panic.panic import *
import sys
from .used import *
from encry.log.log import LogManager
contact="Ofin:||%(level)s"
def gen_key2(level)->str:
    try:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        inf=LogManager("%(func)s"%{"func":func},log_level="INFO")
        if(level!="standard2"and level!="high2"and level!="prof2"and level!="max2"):
            err.error("Invalid level,will be panic")
            raise Panic("%(func)s" %{"func":func},"Invalid level",4,"TypeError").raise_panic()
        leveled=encry_standard(level).decode()
        inf.auto("init level.(convert to base16)")
        contac=contact % {"level":leveled}
        inf.auto("Converting contact(key).....")
        inf.auto("contact: %(contact)s" % {"contact":contact})
        contaced=encry_standard(contac).decode()
        inf.auto("Converted key to base16")
        return contaced
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        err.error(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def to_gen_key2(key=str)->dict:
    try:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        inf=LogManager("%(func)s"%{"func":func},log_level="INFO")
        rege={
            "level":""
        }
        if isinstance(key,str):
            key=key.encode()
        key=decry_standard(key).decode()
        inf.auto("init key succeed.")
        level=decry_standard(key.split(":||")[1].encode()).decode()
        inf.auto(f"Get level succeed.,level: {level}")
        rege['level']=level
        inf.auto("init rege succeed.")
        return rege
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        err.error(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()

