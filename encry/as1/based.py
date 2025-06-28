import pybase64
import base64
class Encry:
    def __init__(self, key):
        self.data = key

    def encry(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry = base64.b64encode(data)
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    def encry_16(self,data):
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry_16 = base64.b16encode(data)
            return self.encry_16
        except Exception as e:
            raise Exception(str(e))
class Decry:
    def __init__(self, key):
        self.data = key

    def decry(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry = base64.b64decode(data)
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    def decry_16(self,data):
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry_16 = base64.b16decode(data)
            return self.encry_16
        except Exception as e:
            raise Exception(str(e))