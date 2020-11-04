import random

userInput=int(input('enter your num, 1-rock, 2-paper, 3-scissor'))
print('You:')
if userInput==1:
    print("rock\n")
elif userInput==2:
    print('paper\n')
elif userInput==3:
    print('scissor\n')
else:
    print('invalid input\n')

print('bot:')
botInput=random.randint(1, 3)
if botInput==1:
    print("rock\n")
elif botInput==2:
    print('paper\n')
elif botInput==3:
    print('scissor\n')

if(userInput==1 and botInput==3) or (userInput==2 and botInput==1) or (userInput==3 and botInput==2):
    print('You win')
elif userInput==botInput:
    print('draw')
else:
    print('You lose')