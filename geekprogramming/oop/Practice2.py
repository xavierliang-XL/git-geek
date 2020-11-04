class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = '[bytetube煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 方法2.1
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 方法2.2
        #super().__init__()
        #super().make_cake()


class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
        super().__init__()
        super().make_cake()

    # 子类调用父类的同名方法和属性：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 一次性调用父类的同名属性和方法
    def make_old_cake(self):
        # 方法一：代码冗余；父类类名如果变化，这里代码需要频繁修改
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # 方法二: super()
        # 方法2.1 super(当前类名, self).函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 方法2.2 super().函数()
        super().__init__()
        super().make_cake()


daqiu = Prentice()
daqiu.make_cake()