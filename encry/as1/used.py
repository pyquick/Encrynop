from encry.as1.based import *

def only_encry_64(data):
    try:
        if not isinstance(data, bytes):
            raise TypeError("Panic:This type is not bytes.")
        a = Encry(data)
        b=a.encry(data)
        return b
    except Exception as e:
        raise Exception(str(e))
def only_encry_16(data):
    try:
        if not isinstance(data, bytes):
            raise TypeError("Panic:This type is not bytes.")
        a = Encry(data)
        b=a.encry_16(data)
        return b
    except Exception as e:
        raise Exception(str(e))
def encry_abve(data):
    try:
        if not isinstance(data, bytes):
            raise TypeError("Panic:This type is not bytes.")

        b=only_encry_64(data)
        c=only_encry_16(b)
        return c
    except Exception as e:
        raise Exception(str(e))
def only_decry_64(data):
    try:
        if not isinstance(data, bytes):
            raise TypeError("Panic:This type is not bytes.")
        a = Decry(data)
        b=a.decry(data)
        return b
    except Exception as e:
        raise Exception(str(e))
def only_decry_16(data):
    try:
        if not isinstance(data, bytes):
            raise TypeError("Panic:This type is not bytes.")
        a = Decry(data)
        b=a.decry_16(data)
        return b
    except Exception as e:
        raise Exception(str(e))
def decry_abve(data):
    try:
        if not isinstance(data, bytes):
            raise TypeError("Panic:This type is not bytes.")
        b=only_decry_16(data)
        c=only_decry_64(b)
        return c
    except Exception as e:
        raise Exception(str(e))