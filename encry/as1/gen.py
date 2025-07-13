from encry.panic.panic import *
import sys
from .used import *
from encry.log.log import LogManager

contact_max_auto="Ofin:||%(level)s!?PUA:||%(tem)s"
contact="Ofin:||%(level)s"
def gen_key(level,tem=None)->str:
    try:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        inf=LogManager("%(func)s"%{"func":func},log_level="INFO")
        if(level!="primary"and level!="standard"and level!="high"and level!="prof"and level!="max"and level!="max_auto"):
            err.error("Invalid level,will be panic")
            raise Panic("%(func)s" %{"func":func},"Invalid level",4,"TypeError").raise_panic()
        leveled=encry_high(level).decode()
        inf.auto("init level.(convert to base16)")
        if (level=="max_auto") and tem==None:
            err.error("Invalid level,will be panic")
            raise Panic("gen","Invalid tem",4,"TypeError").raise_panic()
        if(level=="max_auto"):
            tem=encry_prof(str(tem)).decode()
            inf.auto("convert tem....(convert to base16)")
            contacted=contact_max_auto % {"level":leveled,"tem":tem}
            contac=encry_high(contacted).decode()
            inf.auto("Converted key to base16")
            return contac
        else:
            tem=None
            contac=contact % {"level":leveled}
            inf.auto("Converting contact(key).....")
            inf.auto("contact: %(contact)s" % {"contact":contact})
            contaced=encry_high(contac).decode()
            inf.auto("Converted key to base16")
            return contaced
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        err.error(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def to_gen_key(key=str)->dict:
    try:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        inf=LogManager("%(func)s"%{"func":func},log_level="INFO")
        rege={
            "level":"",
            "tem":None
        }
        if isinstance(key,str):
            key=key.encode()
        key=decry_high(key).decode()
        inf.auto("init key succeed.")
        if "!?" in key:
            key_li=key.split("!?")
            inf.auto("Split key succeed.")
            level=decry_high(key_li[0].split(":||")[1].encode()).decode()
            inf.auto(f"Get level succeed.,level: {level}")
            tem=decry_prof(key_li[1].split(":||")[1].encode()).decode()
            inf.auto(f"Get tem succeed.,tem: {tem}")
            rege['level']=level
            rege["tem"]=tem
            inf.auto("init rege succeed.")
            return rege
        else:
            #print(key.split(":||"))
            level=decry_high(key.split(":||")[1].encode()).decode()
            inf.auto(f"Get level succeed.,level: {level}")
            rege['level']=level
            inf.auto("init rege succeed.")
            return rege
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager("%(func)s"%{"func":func},log_level="ERROR")
        err.error(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()

