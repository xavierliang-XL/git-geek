class Library(object):
    def __init__(self,name,age,ad):
        self.name=name
        self.age=age
        self.ad=ad
        self.capacity=self.ad.update_capacity()

    #show
    def update_capacity(self):
        self.capacity = self.ad.update_capacity()
        print(f"capcity:{self.capacity}")
