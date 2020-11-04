from geekprogramming.lightandbulb.bulb import Bulb
from geekprogramming.lightandbulb.light import Light
class management(object):
    def __init__(self):
        self.light_list=[]
        self.bulb_list=[]
        self.total_income=0

    def menu(self):
        print("all options:")
        print("a.add a light with no bulb, b.add a bulb")
        print("c.delete light, d.delete bulb")
        print("e.search light, f.search bulb")
        print("g.modify light, h.modify bulb")
        print("i.print all lights, j.print all bulbs")
        print("k.sell")
        print("l.save")
        print("m.exit")

    def run(self):
        self.load_light()
        self.load_bulb()
        while True:
            self.menu()
            option=input("whats ur option?")
            if option=='a':
                print(self.add_light())
            elif option=='b':
                print(self.add_bulb())
            elif option=='c':
                print(self.del_light())
            elif option=='d':
                print(self.del_bulb())
            elif option=='e':
                print(self.query_light())
            elif option=='f':
                print(self.query_bulb())
            elif option=='g':
                print(self.modify_light())
            elif option=='h':
                print(self.modify_bulb())
            elif option=='i':
                self.printall_light()
            elif option=='j':
                self.printall_bulb()
            elif option=='k':
                i=int(input("how many lights u wanna sell?"))
                if i > len(self.light_list) or i > len(self.bulb_list):
                    print('not enough bulb or light')
                else:
                    for j in range(i):
                        print(self.sell(0))
            elif option=='l':
                self.save_light()
                self.save_bulb()
            elif option=='m':
                break
            else:
                print('invalid input')

    def add_light(self):
        price=int(input("whats the price of this light?"))
        weight=input("whats the weight of this light?")
        id=input("whats the id of this light?")
        addlight=Light(price, weight,id)
        self.light_list.append(addlight)
        return 'light added'

    def add_bulb(self):
        color=input("whats the color of this bulb")
        price=int(input("whats the price of this bulb?"))
        size=input("whats the size of this bulb?")
        id=input("whats the id of this bulb?")
        addbulb=Bulb(color, size,price,id)
        self.bulb_list.append(addbulb)
        return 'bulb added'

    def del_light(self):
        id=int(input("whats the id of this light?"))
        for i in self.light_list:
            if i.id==id:
                self.light_list.remove(i)
                return 'light removed'
        return 'no such light'

    def del_bulb(self):
        id=int(input("whats the id of this bulb?"))
        for i in self.bulb_list:
            if i.id==id:
                self.bulb_list.remove(i)
                return 'bulb removed'
        return 'no such bulb'

    def modify_light(self):
        id = int(input("whats the id of this light?"))
        for i in self.light_list:
            if i.id == id:
                i.weight=input("weight:")
                i.price=int(input("price:"))
                return 'light modified'
        return 'no such light'

    def modify_bulb(self):
        id = int(input("whats the id of this bulb?"))
        for i in self.bulb_list:
            if i.id == id:
                i.color=input("color:")
                i.size=input("size:")
                i.price=int(input("price:"))
                return 'bulb modified'
        return 'no such bulb'

    def query_light(self):
        id = int(input("whats the id of this light?"))
        for i in self.light_list:
            if i.id == id:
                print(i)
                return 'light found'
        return 'no such light'

    def query_bulb(self):
        id=int(input("whats the id of this bulb?"))
        for i in self.bulb_list:
            if i.id==id:
                print(i)
                return 'bulb found'
        return 'no such bulb'

    def printall_light(self):
        for i in self.light_list:
            print(i)

    def printall_bulb(self):
        for i in self.bulb_list:
            print(i)

    def compose_lightandbulb(self,i):
        print(f'making light{self.light_list[i].id}.....bulb: {self.bulb_list[i]}, price:{self.light_list[i].price+self.bulb_list[i].price}')
        self.light_list[i].bulb=self.bulb_list[i]
        self.light_list[i].price+=self.bulb_list[i].price
        self.bulb_list.remove(self.bulb_list[i])
        print('complete!')
        return self.light_list[i].price

    def sell(self,i):
        income=self.compose_lightandbulb(i)
        self.light_list.remove(self.light_list[i])
        self.total_income+=income
        return f'income: {income}, total: {self.total_income}'

    def load_light(self):
        f = open('lightinfo.txt', 'r')

        data = f.read()

        new_list = eval(data)

        self.light_list = [Light(i['price'], i['weight'],i['id']) for i in new_list]

        f.close()

        print("light information loaded")

    def load_bulb(self):
        f = open('bulbinfo.txt', 'r')

        data = f.read()

        new_list = eval(data)

        self.bulb_list = [Bulb(i['color'], i['size'], i['price'],i['id'])  for i in new_list]

        f.close()

        print("bulb information loaded")

    def save_light(self):
        f = open('lightinfo.txt', 'w')

        new_list = [i.__dict__ for i in self.light_list]

        f.write(str(new_list))

        f.close()

        print("save successful!")

    def save_bulb(self):
        f = open('bulbinfo.txt', 'w')

        new_list = [i.__dict__ for i in self.bulb_list]

        f.write(str(new_list))

        f.close()

        print("save successful!")
