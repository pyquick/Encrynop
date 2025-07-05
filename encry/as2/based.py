from encry.as1.used  import *
from encry.as1.used import  *
from encry.panic.panic import *
from encry.log import *
import sys
lookup={
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    '1000':"8",
    '1001':"9",
    '1010':"A",
    '1011':"B",
    '1100':"C",
    '1101':"D",
    '1110':"E",
    '1111': "F",
}
lookup16={v: k for k, v in lookup.items()}
lookup_check={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
}
lookup_check16={v: k for k, v in lookup_check.items()}
class Convert_Dec:
    def __init__(self, data,convert_base=int,to_convert=int):
        self.data = str(data) #数据
        self.to_convert = to_convert #要被转换的进制
        self.convert_base = convert_base #转换进制基础
        self.result=[]
    def check(self)->bool:
        try:
            self.data_list=list(str(self.data))
            if(self.convert_base>16 or self.to_convert>16): return False
            for i in self.data_list:
                if(lookup_check[str(i)])>self.convert_base-1:
                    return False
            return True
        except Exception:
            return False
    def panic(self):
        self.log=LogManager("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"ERROR")
        if not self.check():
            self.log.error("Decimal data is wrong,will be panic")
            raise Panic("Convert %(func)s"% {"func":sys._getframe().f_code.co_name},"Decimal data is wrong",4,"DecimalError").raise_panic()
    def dec10_convert_to_any(self):
        if(self.check()):
            self.log=LogManager("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"ERROR")
            self.panic()
            if(self.convert_base==10):
                self.data=int(self.data)
            else:
                self.log.auto("Convert_Dec.convert_base>10,Now it is unstopped")
                raise Panic("Convert %(func)s"  % {"func":sys._getframe().f_code.co_name},"Convert_Dec.convert_base>10,Now it is unstopped",3,"DecimalError").raise_panic()
            self.data_in=self.data
            while(self.data_in>0):
                if(self.data_in%self.to_convert>=10):
                    self.result.append(lookup_check16[self.data_in%self.to_convert])
                else:
                    self.result.append(str(self.data_in%self.to_convert))
                self.data_in//=self.to_convert
            self.result=self.result[::-1]
            self.result_send=""
            for i in self.result:
                self.result_send+=i
            return self.result_send
        else:
            self.panic()
    def dec_16_to_2(self):
        if(self.convert_base!=16 or self.to_convert!=2):
            self.log=LogManager("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"ERROR")
            self.log.auto("Decimal data is wrong,will be panic")
            raise Panic("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"Decimal data is wrong",3,"DecimalError").raise_panic()
        self.panic()
        self.data_list=list(str(self.data))
        self.result=[]
        self.result_send=""
        for i in range(len(self.data_list)):
            self.result.append(str(lookup16[str(self.data_list[i])]))
        for i in self.result:
            self.result_send+=i
        return int(self.result_send)
    def dec_2_to_16(self):
        if(self.convert_base!=2 or self.to_convert!=16):
            self.log=LogManager("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"ERROR")
            self.log.auto("Decimal data is wrong,will be panic")
            raise Panic("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"Decimal data is wrong",3,"DecimalError").raise_panic()
        self.panic()
        self.data=str(self.data)
        if(len(self.data)%4!=0):
            while(True):
                self.data="0"+self.data
                if(len(self.data)%4==0):
                    break
        self.result=[]
        self.result_send=""
        self.crashe=[""]
        self.x=0
        for i in range(len(self.data)):
            self.crashe[self.x]+=self.data[i]
            if(i+1)%4==0 and i!=len(self.data)-1:
                self.x+=1
                self.crashe.append("")
        for i in range(len(self.crashe)):
            self.result.append(lookup[self.crashe[i]])
        for i in self.result:
            self.result_send+=i
        return self.result_send
    def dec_8_to_2(self):
        if(self.convert_base!=8 or self.to_convert!=2):
            self.log=LogManager("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"ERROR")
            self.log.auto("Decimal data is wrong,will be panic")
            raise Panic("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"Decimal data is wrong",3,"DecimalError").raise_panic()
        self.panic()
        self.data=list(str(self.data))
        self.result=[]
        self.result_send=""
        for i in range(len(self.data)):
            self.fun=str(int(lookup16[str(self.data[i])]))
            if(len(self.fun)<3):
                while(len(self.fun)<3):
                    self.fun="0"+self.fun
            self.result.append(self.fun)
        for i in self.result:
            self.result_send+=i
        return int(self.result_send)
    def dec_2_to_8(self):
        if(self.convert_base!=2 or self.to_convert!=8):
            self.log=LogManager("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"ERROR")
            self.log.auto("Decimal data is wrong,will be panic")
            raise Panic("Convert %(func)s" % {"func":sys._getframe().f_code.co_name},"Decimal data is wrong",3,"DecimalError").raise_panic()
        self.panic()
        self.data=str(self.data)
        if(len(self.data)%3!=0):
            while(True):
                self.data="0"+self.data
                if(len(self.data)%3==0):
                    break
        self.result=[]
        self.result_send=""
        self.crashe=[""]
        self.x=0
        for i in range(len(self.data)):
            self.crashe[self.x]+=self.data[i]
            if(i+1)%3==0 and i!=len(self.data)-1:
                self.x+=1
                self.crashe.append("")
        for i in range(len(self.crashe)):
            self.fun=str(int(self.crashe[i]))
            while(len(self.fun)<4):
                self.fun="0"+self.fun
            self.result.append(lookup[self.fun])
        for i in self.result:
            self.result_send+=i
        return self.result_send
    
    
    
            
        
    