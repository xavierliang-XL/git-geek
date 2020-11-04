#get user input: username ,password
#print username ,password
def login():
    """
    this method is to do the process of logging in by checking username and password
    """
    db_user_name = "dal"
    db_password = "111111"
    user_name = input("plz input your username:")
    password = input("plz input your password:")
    if user_name==db_user_name and db_password==password:
        return(user_name+"! Welcome")
    else:
        print("plz check your username or password")
