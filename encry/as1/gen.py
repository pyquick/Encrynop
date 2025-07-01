#生成as1符合规范的规定(让gui识别)
from .used import *
contact_max_auto="Ofin:||%(level)s!?PUA:||%(tem)s"
contact="Ofin:||%(level)s"
def gen(level=str,tem=str|None)->bytes:
    leveled=encry_standard(level).decode()
    if(level=="max_auto"):
        tem=encry_prof(str(tem)).decode()
        return encry_standard(contact_max_auto % {"level":leveled,"tem":tem})
    else:
        tem=None
        return encry_standard(contact % {"level":leveled})

def regen(key=bytes)->dict:
    rege={
        "level":"",
        "tem":None
    }
    key=decry_standard(key).decode()
    
    if "!?" in key:
        key_li=key.split("!?")
        level=decry_standard(key_li[0].split(":||")[1].encode()).decode()
        tem=decry_prof(key_li[1].split(":||")[1].encode()).decode()
        rege['level']=level
        rege["tem"]=tem
        return rege
    else:
        print(key.split(":||"))
        level=decry_standard(key.split(":||")[1].encode()).decode()
        rege['level']=level
        return rege

