import random
#random.randint(min,max)
computer = random.randint(0,2)
print(computer)

player=int(input('lets go：0-rock，1-scissors，2-paper：'))
#player win
def rPS(player,computer):
    """
    this method is to judge the result of game of getting the two values of player and computer
    player:user's input
    computer:random number
    """
    if((player==0)and (computer==1) or (player==1)and (computer==2) or (player==2)and (computer==0)):
        return "player win"
#tied game
    elif player==computer:
        return "tied game "
#computer win
    else:
        return "computer win"