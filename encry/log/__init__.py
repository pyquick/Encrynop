from encry.panic.panic import *
from .log import *
from .limit import *
import threading
a=threading.Thread(target=Limit_Size(136314880,36700160).limit_size())
a.start()
a.join()
