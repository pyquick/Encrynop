from encry.as1.used  import *
from encry.as1.used import  *
lookup={
    0:"0",
    1:"1",
    10:"2",
    11:"3",
    100:"4",
    101:"5",
    110:"6",
    111:"7",
    1000:"8",
    1001:"9",
    1010:"A",
    1011:"B",
    1100:"C",
    1101:"D",
    1110:"E",
    1111: "F",
}
lookup16={
    "0":0,
    "1":1,
    "2":10,
    "3":11,
    "4":100,
    "5":101,
    "6":110,
    "7":111,
    "8":1000,
    "9":1001,
    "A":1010,
    "B":1011,
    "C":1100,
    "D":1101,
    "E":1110,
    "F":1111
}

class Convert:
    def __init__(self, data,to_convert,convert_base):

        self.data = data
        self.to_convert = to_convert
        self.convert_base = convert_base
    def check(self,convert_base,to):
        #判断进制是否合法
        pass

    def convert(self):
        pass
    def to_convert_st(st) -> list:  #
        stl = list(str(st))

        for i in range(0, len(stl)):
            stl[i] = str(lookup16[stl[i]])
        return stl