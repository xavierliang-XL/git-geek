account_info=[]
def add_account():
    name=input('whats ur name?')
    id=input('input ur id')
    grade=int(input('ur grade(0~100)'))
    for i in account_info:
        if i['name']==name or i['id'] == id or i['grade']==grade:
            print('duplicate account')

    info_dict={}
    info_dict['name']=name
    info_dict['id']=id
    info_dict['grade']=grade
    account_info.append(info_dict)
    print(f"account {info_dict['name']} has been added")

def del_account():
    id=input("whats the user's id?")
    global account_info
    for i in account_info:
        if i['id']==id:
            account_info.remove(i)
            print(f"account {i['name']} has been deleted")
            break
        else:
            print('account does not exist')

def modify_account():
    id=input("whats ur modify id?")
    for i in account_info:
        if i['id']==id:
            i['grade']=input("ur mark?")
            print(f"account {i['name']} has been updated")
            break
        else:
            print("doesn't exist")

def search_account():
    id=input('whars ur id?')
    global account_info
    for i in account_info:
        if i['id']==id:
            print(i)
            break
        else:
            print("doesn't exist")

def search_accounts():
    global account_info
    if len(account_info) == 0:
        print('there is no account')
    else:
        for i in account_info:
            print(f"account_id:{i['id']}, account_name:{i['name']}, account_grade:{i['grade']}")

def menu():
    print('1.add user')
    print('2.del user')
    print('3.modify user')
    print('4.query user by id')
    print('5.query all users')
    print('6.exit')

def get_user_input():
    num=int(input('plz select #:'))
    if num==1:
        add_account()
    elif num==2:
        del_account()
    elif num==3:
        modify_account()
    elif num==4:
        search_account()
    elif num==5:
        search_accounts()
    elif num==6:
        return False
    else:
        print('invalid input')

def driver():
    while True:
        menu()
        res=get_user_input()
        if res==False:
            break
driver()
