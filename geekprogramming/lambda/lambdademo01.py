students=[{'name':'Tom','grade':100},{'name':'ROSE','grade':90},{'name':'Jack','grade':190}]
students.sort(key=lambda i: i['grade'], reverse=True)
for i in range(1,len(students)+1):
    print(f"name:{students[i-1]['name']}, rank:{i}，grade:{students[i-1]['grade']}")