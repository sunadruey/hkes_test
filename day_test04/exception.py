class MyException(Exception):
    def __init__(self,msg):
        print(f"这是一个异常 ：{msg}")
