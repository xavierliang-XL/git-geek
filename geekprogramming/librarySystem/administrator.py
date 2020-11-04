from geekprogramming.librarySystem.categoriesAndBook import book,category
from geekprogramming.librarySystem.library import library
import random

class administrator(object):
    def __init__(self,id,name):
        self.aid=id
        self.aname=name
        self.level=random.randint(1,10)

    def run(self,library):
        breaking=True
        while breaking:
            self.menu()
            de=input("whats ur decision?")
            if de=="1":
                de=input("add book or add category? a to add book, b to add category")
                if de == "a":
                    print(self.add_book(library))
                elif de=="b":
                    print(self.add_category(library))
                else:
                    print("invalid input")
            elif de=="2":
                de = input("remove book or category? a to remove book, b to remove category")
                if de =="a":
                    print(self.remove_book(library))
                elif de=="b":
                    print(self.remove_category(library))
                else:
                    print("invalid input")
            elif de =="3":
                de=input("update book or category? a to update book, b to update category")
                if de =="a":
                    print(self.update_book(library))
                elif de=="b":
                    print(self.update_category(library))
                else:
                    print("invalid input")
            elif de=="4":
                print("a to search book by category, b to search book by name, c to search book by id")
                print("d to search all books, e to search all categories")
                de=input("ur choice?")
                if de =="a":
                    print(self.search_by_category(library))
                elif de=="b":
                    print(self.search_by_bname(library))
                elif de=="c":
                    print(self.search_by_bid(library))
                elif de=="d":
                    print(self.search_all_books(library))
                elif de=="e":
                    print(self.search_all_categories(library))
                else:
                    print("invalid input")
            elif de=="5":
                self.show_capacity(library)
            elif de=="6":
                breaking=False
            else:
                print("invalid choice")


    def menu(self):
        print("1.add: a.add book b.add category")
        print("2.remove: a.remove book b.remove category")
        print("3.update: a. update book b.update category")
        print("4.search: a.search book by category, b.search by book name, c.search by book id")
        print("d.search all books e.search all categories")
        print("5.show capacity")
        print("6.exit")

    def show_capacity(self,library):
        return library.capacity

    def add_book(self,library):
        if len(library.categories)<=0:
            return "no category, add a category before u add book"
        else:
            id=input("id:")
            for i in library.book_list:
                if i.bid==id:
                    return "duplicate id"
            name=input("name:")
            author=input("author:")
            category=input("id of the category:")
            for i in library.categories:
                if i.cid==category:
                    Book=book(name,id,author,i,"2020-08-20")
                    library.book_list.append(Book)
                    library.update_capacity()
                    return f"book added"
            return "no such category"


    def add_category(self,library):
        id=input("id:")
        for i in library.categories:
            if i.cid == id:
                return "duplicate id"
        name=input("name:")
        Category=category(id,name)
        library.categories.append(Category)
        return "category added"

    def remove_book(self,library):
        id=input("what book u want to delete?")
        for i in library.book_list:
            if i.bid==id:
                library.book_list.remove(i)
                return f"book {i.bname} removed"
        return "no such book"

    def remove_category(self,library):
        id=input("what book u want to delete?")
        for i in library.categories:
            if i.cid==id:
                library.categories.remove(i)
                return f"category {i.cname} removed"
        return f"no such category"

    def update_book(self,library):
        id=input("whats the id of the book?")
        for i in library.book_list:
            if i.bid==id:
                print(f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category.cname}")
                name=input("whats the new name of this book?")
                author=input("new author?")
                publish_date=input("new publish date?")
                category=input("new category id?")
                for j in library.categories:
                    if category==j.cid:
                        i.bname,i.author,i.publish_date,i.category = name,author,publish_date,j
                        return "book changed"
                return "no such category"
        return "no such book"


    def update_category(self,library):
        id=input("whats the id of the category?")
        name=input("whats its new name?")
        for i in library.categories:
            if i.cid==id:
                i.cname=name
                return "category changed"
        return "no such category"

    def search_by_category(self,library):
        id=input("input the id of category:")
        for i in library.categories:
            if id==i.cid:
                name=i.cname
                for i in library.book_list:
                    if name==i.category:
                        return f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category.cname}"
        return "no such book"

    def search_by_bname(self,library):
        name=input("enter book name:")
        for i in library.book_list:
            if i.bname==name:
                return f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category.cname}"
        return "no such book"

    def search_by_bid(self,library):
        id=input("enter book id:")
        for i in library.book_list:
            if i.bid==id:
                return f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category.cname}"
        return "no such book"

    def search_all_books(self,library):
        for i in library.book_list:
            print(f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category.cname}")
        return "book printed"

    def search_all_categories(self,library):
        for i in library.categories:
            print(f"name:{i.cname} id:{i.cid}")
        return "categories printed"


