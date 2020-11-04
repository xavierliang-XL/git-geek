class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def sleep(self):
        print("zzzzzzzzzz")
    def run(self):
        print(f'{self.name} is running')
    def get_Age(self):
        return self.__age
    def set_Age(self,age):
        self.__age=age

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.__student_id=student_id
    def study(self):
        print(f'{self.__student_id} is studying')

    def run(self):
        super().run()
        print(f'{self.__student_id} is running')

stu=Student('David',13,1)
stu.run()