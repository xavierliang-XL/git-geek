#abcdef  ==> ace
#012345
str = input("plz input a word")
def digits(str):
    """
    this method is to get the strings from even digits
    str:original string
    """
    new_str=""
    for i in range(len(str)):
        if i%2==0:
            new_str+=str[i]


    return(new_str)