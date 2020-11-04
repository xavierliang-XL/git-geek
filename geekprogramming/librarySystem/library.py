class library(object):
    def __init__(self,name,age):
        self.name=name
        self.book_list=[]
        self.age=age
        self.categories=[]
        self.capacity=len(self.book_list)

    def update_capacity(self):
        self.capacity = len(self.book_list)
