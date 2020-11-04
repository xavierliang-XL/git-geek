class Doge():
    def __init__(self,weight,age):
        self.weight=weight
        self.age=age

    def __str__(self):
        return "[Doge]"

cado=Doge(50,2)
print(cado)