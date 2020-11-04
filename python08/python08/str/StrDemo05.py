#List:[beginIndex:endIndex:len]
str="abcdefg"
    #0123456
def strIndex(str) :
    """
    this method is to return string that is composed by part of the original string
    str:original string
    """
    return str[2:5],str[2:5:2],str[5:],str[0::2],str[::-2]#cde [beginIndex,endIndex)<===>[beginIndex,endIndex-1]