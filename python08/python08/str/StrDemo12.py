# remove space from str
# Da vi d ==>David
user_input = input("plz input a word")
def space(user_input):
    """
    this method is to remove the blanks from a string
    user_input:string
    """
    user_input=user_input.replace(" ","")
    return(user_input)
