grade=input("whats ur grade?")
if grade.isnumeric():
    grade=int(grade)
    res="excellent"if grade >= 90 else "good"if grade >= 75 else "pass"if grade >= 60 else "fail"
    print(res)
else:
    print("invalid input")