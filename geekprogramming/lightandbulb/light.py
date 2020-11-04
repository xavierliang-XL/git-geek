import geekprogramming.lightandbulb.bulb

class Light(object):
    def __init__(self,price,weight,id):
        self.bulb=None
        self.price=price
        self.weight=weight
        self.id=id

    def __str__(self):
        return f'bulb: {self.bulb},price: {self.price},weight: {self.weight},id: {self.id}'