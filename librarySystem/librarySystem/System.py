from librarySystem.Administrator import Administrator
from librarySystem.Library import Library
ad=Administrator(1,"jim")
library=Library("jim library",100,ad)
class System(object):
    global ad
    global library

    def menu(self):
        print("1.add: a.add book b.add category")
        print("2.remove: a.remove book b.remove category")
        print("3.update: a. update book b.update category")
        print("4.search: a.search book by category, b.search by book name, c.search by book id")
        print("d.search all books e.search all categories")
        print("5.exit")

    def run(self):
        breaking=True
        ad.load_books()
        ad.load_categories()
        while breaking:
            self.menu()
            library.update_capacity()
            de=input("whats ur decision?")
            if de=="1":
                de=input("add book or add category? a to add book, b to add category")
                if de == "a":
                    print(ad.add_book())
                elif de=="b":
                    print(ad.add_category())
                else:
                    print("invalid input")
            elif de=="2":
                de = input("remove book or category? a to remove book, b to remove category")
                if de =="a":
                    print(ad.remove_book())
                elif de=="b":
                    print(ad.remove_category())
                else:
                    print("invalid input")
            elif de =="3":
                de=input("update book or category? a to update book, b to update category")
                if de =="a":
                    print(ad.update_book())
                elif de=="b":
                    print(ad.update_category())
                else:
                    print("invalid input")
            elif de=="4":
                print("a to search book by category, b to search book by name, c to search book by id")
                print("d to search all books, e to search all categories")
                de=input("ur choice?")
                if de =="a":
                    print(ad.search_by_category())
                elif de=="b":
                    print(ad.search_by_bname())
                elif de=="c":
                    print(ad.search_by_bid())
                elif de=="d":
                    print(ad.search_all_books())
                elif de=="e":
                    print(ad.search_all_categories())
                else:
                    print("invalid input")
            elif de=="5":
                de=input("save changes? yes or no")
                if de=="yes":
                    ad.save_categories()
                    ad.save_books()
                    print("data saved")
                breaking=False
            else:
                print("invalid choice")