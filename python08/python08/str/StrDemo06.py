#abc
#abcing
#abcingly
def ingly():
    """
    this method is to add 'ing' if 'ing' does not appear at the end of a word or 'ly' if 'ing' does appear at the end of a word
    """
    str=input("plz input a word:")
    if str[-3:]=="ing":
        str = str+"ly"
    else:
        str = str + "ing"
    return(str)
