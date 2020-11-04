class Singleton(object):
    __instance=None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")

        else:
            print("__instance already exist",self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance=Singleton()

        return cls.__instance


s1=Singleton()
print("first obj created", Singleton.get_instance())

s2=Singleton()
print("second obj created", s2)