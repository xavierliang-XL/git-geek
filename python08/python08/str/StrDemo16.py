str1="byte"
str2="tube"
str3="by"
str4="dal"
#print(str1.join(str2))#tbyteubytebbytee
    # str1      str2
    #str2

str = "hello world and hello bytetube and hello dal and hello python and"
#print(str.split("and"))
def joinAnd(str):
    """
    the method is to add and in the interval of each string
    str:String
    """
    return("and".join(str.split("and")))

#www.amazon.com
list=["www","amazon","com"]
print(".".join(list))