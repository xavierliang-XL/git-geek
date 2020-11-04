class Student(object):
    def __init__(self,name,gender,grade):
        self.name=name
        self.gender=gender
        self.grade=grade
    def __str__(self):
        return f'{self.name},{self.gender},{self.grade}'