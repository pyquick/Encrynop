from encry.as1.based import *

def encry_64(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry(data)
        b=a.encry(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_85(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry(data)
        b=a.encry_85(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_32(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry(data)
        b=a.encry_32(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_16(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry(data)
        b=a.encry_16(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()

def decry_64(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry(data)
        b=a.decry(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def decry_16(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry(data)
        b=a.decry_16(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def decry_32(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry(data)
        b=a.decry_32(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def decry_85(data):
    try:
        if not isinstance(data, bytes):
            raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry(data)
        b=a.decry_85(data)
        return b
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_primary(data):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        data_encryed=encry_64(data)
        data_encryed=encry_16(data_encryed)
        return data_encryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def decry_primary(data):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        data_decryed = decry_16(data)
        data_decryed=decry_64(data_decryed)
        return data_decryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_standard(data):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        data_encryed=encry_85(data)
        data_encryed=encry_32(data_encryed)
        data_encryed = encry_16(data_encryed)
        return data_encryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_high(data):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        data_encryed=encry_85(data)
        data_encryed = encry_64(data_encryed)
        data_encryed=encry_32(data_encryed)
        data_encryed = encry_64(data_encryed)
        data_encryed = encry_16(data_encryed)
        return data_encryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def decry_high(data=str|bytes):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        data_decryed = decry_16(data)
        data_decryed = decry_64(data_decryed)
        data_decryed=decry_32(data_decryed)
        data_decryed = decry_64(data_decryed)
        data_decryed=decry_85(data_decryed)
        return data_decryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_prof(data):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        for i in range(20):
            data_encryed=encry_85(data)
            data_encryed = encry_64(data_encryed)
        data_encryed=encry_32(data_encryed)
        data_encryed = encry_64(data_encryed)
        data_encryed = encry_16(data_encryed)
        return data_encryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_max(data):
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        for i in range(100):
            data_encryed=encry_85(data)
            data_encryed = encry_64(data_encryed)

        for i in range(50):
            data_encryed=encry_32(data_encryed)
            data_encryed = encry_64(data_encryed)
        data_encryed=encry_64(data_encryed)
        data_encryed = encry_32(data_encryed)
        data_encryed = encry_16(data_encryed)
        return data_encryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()
def encry_max_auto(data):
    #不推荐使用
    try:
        if not isinstance(data, bytes):
            data=data.encode()
        for i in range(pow(len(data),2)):
            data_encryed=encry_85(data)
            data_encryed = encry_64(data_encryed)
        for i in range(pow(len(data),2)):
            data_encryed=encry_32(data_encryed)
            data_encryed = encry_64(data_encryed)
        data_encryed = encry_16(data_encryed)
        return data_encryed
    except Exception as e:
        raise Panic(str(e),4,"Exception").raise_panic()