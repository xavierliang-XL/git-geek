from geekprogramming.librarySystem.administrator import administrator
from geekprogramming.librarySystem.library import library



if __name__=='__main__':
    ad = administrator(1, "jim")
    lib = library("a", 10)
    ad.run(lib)