grading=eval(input("plz enter your mark"))
if (grading>=85) and (grading<=100):
    print("A")
elif (grading >= 75) and (grading < 85):
    print("B")
elif (grading >= 60) and (grading < 75):
    print("C")
elif (grading < 60) and (grading>=0):
    print("D")
else:
    print("invalid input")
