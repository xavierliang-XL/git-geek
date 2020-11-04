import random
num=random.randint(0,100)
uI = int(input("plz enter your input:"))

while uI!=num:
    if uI<num:
        print('smaller')
    elif uI>num:
        print('bigger')
    uI = int(input("plz enter your input:"))


print('bingo')
