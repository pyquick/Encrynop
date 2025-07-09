from encry.as1.used import *
from encry.as2.based import *
from encry.log import *
from encry.panic import *
ascii=ASCII()
def encry_ascii(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data_list=list(data)
        inf.auto(f"Convert data to list successfully . data_list: {data_list}")
        inf.auto("Preparing to convert to ascii.....")
        for i in range(len(data_list)):
            data_list[i]=ascii.to_ascii()
            inf.auto("Converting base16 char to ascii....")
            inf.auto(f"data_list[{i}]:{data_list[i]}")
            inf.auto(f"data_list: {data_list}")
        sb=""
        inf.auto("")
        for i in data_list:
            sb+=i+"|"
        sb=sb.rstrip(" | ")
        return sb
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        err.auto(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE")
    
    
def decry_ascii(data=str):
    data_list=data.split("|")
def encry_standard2(data):
    #转换一次为ascii以及二进制
    #首先转换为ascii
    
    data=encry_ascii(data)
    dec=Convert_Dec(data,16,2)
    data=dec.convert()
    return data
def decry_standard2(data): 
    dec=Convert_Dec(data,2,16)
    data=dec.convert()
    data=ascii.from_ascii(data)
    return data
def encry_high2(data):
    #转换为ascii两次,转换16-9-5-4-2
    data=encry_prof(data).decode()
    data=ascii.to_ascii(data)
    for i in range(4):
        if i==0:
            begin=16
            func=9
        if i==1:
            begin=9
            func=5
        if i==2:
            begin=5
            func=4
        if i==3:
            begin=4
            func=2
        data=Convert_Dec(data,begin,func).convert()
    return data
def decry_high2(data):
    for i in range(4):
        if i==0:
            begin=2
            func=4
        if i==1:
            begin=4
            func=5
        if i==2:
            begin=5
            func=9
        if i==3:
            begin=9
            func=16
        data=Convert_Dec(data,begin,func).convert()
    data=ascii.from_ascii(data)
    data=decry_prof(data).decode()
    return data


        
          
        
    
    