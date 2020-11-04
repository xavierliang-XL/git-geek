import random

money=input('do you have money? 1.yes 2.no')
seat=random.randint(1,2)

if money=='1':
    money=True
elif money=='2':
    money=False
else:
    print('invalid input')

if seat==1:
    seat=True
else:
    seat=False

if money==True:
    print('you are able to get on the bus')
    if seat==True:
        print('you are able to sit down')
    else:
        print('you cannot sit down')
else:
    print('you cannot get on the bus')
print('over')

