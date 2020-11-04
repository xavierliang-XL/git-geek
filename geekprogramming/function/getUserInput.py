user_input=input('input whatever you want:')

def getUserInput(user_input):
    user_input = f'user input:{user_input}' if user_input.isalpha() else eval(user_input) * 2
    return user_input

print(getUserInput(user_input))