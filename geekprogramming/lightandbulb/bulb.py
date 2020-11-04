
class Bulb(object):
    def __init__(self,color,size,price,id):
        self.color=color
        self.size=size
        self.price=price
        self.id=id

    def __str__(self):
        return f'color: {self.color},size: {self.size},price: {self.price},id: {self.id}'