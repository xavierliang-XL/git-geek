class book(object):
    def __init__(self,name,id,author,category,publish_date):
        self.bname=name
        self.bid=id
        self.author=author
        self.publish_date=publish_date
        self.category=category


class category(object):
    def __init__(self,id,name):
        self.cid=id
        self.cname=name
