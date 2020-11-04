str = "hello world and hello bytetube and hello dal and hello python"
# print(str.find("java"))
# print(str.find("and",13))
#find() return target str index
str_len = len(str)
print(str_len)
def findTheAndWord(str):
    """
    the method is to find the 'and' word by using begin index and end index from a string
    str:string
    """
    return(str.index("and",32,len(str)))#param1 target str, param2 beginIndex,param3 endIndex