import random
class Home():
    furniture_number=0
    def __init__(self,address,area):
        self.address=address
        self.area=area
        self.free_area=area
        self.furniture=[]
    def add_furniture(self,furniture):
        self.furniture_number += 1
        if type(furniture)!=Furniture:
            return False
        self.furniture.append(f"{furniture.name}'s size:{furniture.size}")
        self.free_area-=furniture.size
        print(f"{furniture.name} added, size:{furniture.size}, free_area remaining:{self.free_area} continue")



class Furniture():
    def __init__(self,size):
        self.name=self.getname_furniture()
        self.size=size

    def getname_furniture(self):
        pick=random.randint(1,10)
        if pick<3:
            return "light"
        elif pick<5:
            return "table"
        elif pick<7:
            return "chair"
        elif pick<9:
            return "electronic device"
        else:
            return "bed"
home=Home("8848 midland area",50)
while home.free_area>0:
    furniture=Furniture(random.randint(1,10))
    if furniture.size>home.free_area:
        break
    home.add_furniture(furniture)
print(f"total furniture added:{home.furniture}")
print('no free area, over')