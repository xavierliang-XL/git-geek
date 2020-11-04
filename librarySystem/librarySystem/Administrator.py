from librarySystem.Book import Book
from librarySystem.Category import Category
books = []
categories = []
class Administrator(object):
    global books
    global categories
    def __init__(self, aid, aname):
        self.aid = aid
        self.aname = aname
        self.level = 1

    #library--->global
    #categories--->global
    #books--->global

    def update_capacity(self):
        return len(books)

    def add_book(self):
        if len(categories)<=0:
            print( "no category, add a category before u add book")
            self.add_category()
            print("category added")
            return self.add_book()
        else:
            id=input("id:")
            for i in books:
                if i.bid==id:
                    return "duplicate id"
            name=input("name:")
            author=input("author:")
            category=input("id of the category:")
            for i in categories:
                if i.cid == category:
                    book = Book(name, id, author, i.cname, "2020-08-20")
                    books.append(book)
                    return "book added"
            return "no such category"


    def add_category(self):
        id=input("id:")
        for i in categories:
            if i.cid == id:
                return "duplicate id"
        name=input("name:")
        category=Category(id,name)
        categories.append(category)
        return "category added"

    def remove_book(self):
        id=input("what book u want to delete?")
        for i in books:
            if i.bid==id:
                books.remove(i)
                return f"book {i.bname} removed"
        return "no such book"

    def remove_category(self):
        id=input("what book u want to delete?")
        for i in categories:
            if i.cid==id:
                categories.remove(i)
                return f"category {i.cname} removed"
        return f"no such category"

    def update_book(self):
        id=input("whats the id of the book?")
        for i in books:
            if i.bid==id:
                print(f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category}")
                name=input("whats the new name of this book?")
                author=input("new author?")
                publish_date=input("new publish date?")
                category=input("new category id?")
                for j in categories:
                    if category==j.cid:
                        i.bname,i.author,i.publish_date,i.category = name,author,publish_date,j.cname
                        return "book changed"
                return "no such category"
        return "no such book"


    def update_category(self):
        id=input("whats the id of the category?")
        name=input("whats its new name?")
        for i in categories:
            if i.cid==id:
                i.cname=name
                return "category changed"
        return "no such category"

    def search_by_category(self):
        id=input("input the id of category:")
        for i in categories:
            if id==i.cid:
                for j in books:
                    if i.cname==j.category:
                        return f"name:{j.bname} id:{j.bid} author:{j.author} publish date:{j.publish_date} category:{j.category}"
        return "no such book"

    def search_by_bname(self):
        name=input("enter book name:")
        for i in books:
            if i.bname==name:
                return f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category}"
        return "no such book"

    def search_by_bid(self):
        id=input("enter book id:")
        for i in books:
            if i.bid==id:
                return f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category}"
        return "no such book"

    def search_all_books(self):
        for i in books:
            print(f"name:{i.bname} id:{i.bid} author:{i.author} publish date:{i.publish_date} category:{i.category}")
        return "book printed"

    def search_all_categories(self):
        for i in categories:
            print(f"name:{i.cname} id:{i.cid}")
        return "categories printed"

    def save_books(self):
        f=open('Books.txt', 'w')

        list=[i.__dict__ for i in books]

        f.write(str(list))

        f.close()

    def save_categories(self):
        f=open('Categories.txt', 'w')

        list=[i.__dict__ for i in categories]

        f.write(str(list))

        f.close()

    def load_books(self):
        f = open('Books.txt', 'r')

        data=f.read()

        list=eval(data)

        global books

        books=[Book(i['bname'],i['bid'],i['author'],i['category'],i['publish_date']) for i in list]

        f.close()

    def load_categories(self):
        f = open('Categories.txt', 'r')

        data=f.read()

        list=eval(data)

        global categories

        categories=[Category(i['cid'],i['cname']) for i in list]

        f.close()



