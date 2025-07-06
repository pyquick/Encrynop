import sys,threading
import threading
import inspect
def  abc():
    print("abc")
def my_function():
    function_name = sys._getframe().f_code.co_name
    print(f"当前函数名称: {function_name}")

def target_function():
    print(1)

def calling_function():
    # 获取模块中的函数对象
    function_obj = inspect.getmodule(inspect.currentframe()).target_function 
    my_function() # 获取当前模块的目标函数对象
    return function_obj.__name__  # 输出: 目标函数名称: target_function
def myi_function():
    print(f"线程执行中: {threading.current_thread().name}")
# 获取函数对象（推荐方式）
#function_obj = inspect.getmodule(inspect.currentframe()).my_function
# 创建线程并传递函数对象
#thread = threading.Thread(target=function_obj)
#thread.start()





