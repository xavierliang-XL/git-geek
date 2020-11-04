#input()接收用户输入的数据类型都是 字符串类型str--->int
num = input("plz input:")

def sout(val):
    """
    this method is to return the type of value
    val:any kind of value
    """
    return val,type(val)
sout(num)