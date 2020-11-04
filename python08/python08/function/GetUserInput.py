#如果用户输入的是string(david)---> user input string:david
#如果用户输入的是int(10)---> 10*2
#str.isdigit()
#str.isalpha()
# user_input = input("plz input:")
#
# if user_input.isalpha():
#     print(f"UserInput String:{user_input}")
# elif user_input.isdigit():
#     user_input = eval(user_input)*2
#     print(user_input)
# else:
#     print("plz check your input")

def getUserInput():
    """
    this method is to get user's input and judge its type
    """
    user_input = input("plz input:")

    if user_input.isalpha():
        print(f"UserInput String:{user_input}")
    elif user_input.isdigit():
        user_input = eval(user_input) * 2
        print(user_input)
    else:
        print("plz check your input")



getUserInput()