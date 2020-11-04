from geekprogramming.StudentAccountManageSystem.student import Student


class managementSystem(object):

    def __init__(self):
        self.student_list=[]

    def run(self):
        self.load_stu()
        while True:
            self.show_menu()
            number=int(input("plz choose ur option:1~7"))
            if number == 1:
                print(self.add_stu())
            elif number==2:
                print(self.del_stu())
            elif number==3:
                print(self.modify_stu())
            elif number==4:
                print(self.query_stu())
            elif number==5:
                self.show_all()
            elif number==6:
                self.save_stu()
            elif number==7:
                break
#增
#删
#改
#查

    def show_menu(self):
        print("plz select the option that you need:")
        print('1.add student')
        print('2.del student')
        print('3.modify student')
        print('4.query student')
        print('5.show all students info')
        print('6.save student info')
        print('7.exit')

    def add_stu(self):
        name=input("plz input student's name")
        gender=input("plz input student's gender")
        grade=input("plz input student's grade")
        student=Student(name,gender,grade)
        self.student_list.append(student)
        print(self.student_list)

    def del_stu(self):
        name=input("what's the name of student?")
        for i in self.student_list:
            if i.name==name:
                self.student_list.remove(i)
                return f"student {i.name} deleted"
        return 'no such student'

    def modify_stu(self):
        name=input("what's the new name of student?")
        for i in self.student_list:
            if i.name==name:
                i.name=input('name:')
                i.gender=input('gender:')
                i.grade=input('grade:')
                return f"student {i.name} modified"
        return 'no such student'

    def query_stu(self):
        name=input("what's the name of the student")
        for i in self.student_list:
            if i.name==name:
                return f'{i.name}, {i.gender}, {i.grade}'
        return 'no such student'

    def show_all(self):
        for i in self.student_list:
            print(i)

    def save_stu(self):
        f=open('studentinfo.txt', 'w')

        new_list=[i.__dict__ for i in self.student_list]

        f.write(str(new_list))

        f.close()

    def load_stu(self):
        f = open('studentinfo.txt', 'r')

        data=f.read()

        new_list=eval(data)

        self.student_list=[Student(i['name'],i['gender'],i['grade']) for i in new_list]

        f.close()
