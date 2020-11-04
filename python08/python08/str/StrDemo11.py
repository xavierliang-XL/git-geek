#the taste is not xxx poor!
#the taste is good!
#the taste is poor!
#the taste is poor
def goodAndPoor():
    """
    this method is to replace 'not poor' to 'good'
    """
    str="the taste is poor"
    snot = str.find("not")
    print(snot)
    spoor = str.find("poor")

    if spoor> snot and snot>0:
        str = str.replace(str[snot:(spoor+4)],"good")
        return(str)
    else:
        return(str)