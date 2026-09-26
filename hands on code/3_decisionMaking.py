
# conditional statements - if, if-else, if-elif-else

marks=101
if(marks>=90 and marks <=100):
    print("you got A+")
    if(marks>=95):
        print(f"you score {marks} which is outstanding!!!")
        print("keep it up")
elif (marks>=80 and marks<=90):
    print("Grade A")
elif(marks >=70 and marks<80):
    print("Grade B")
elif(marks>=60 and marks<70):
    print("Grade C")
elif(marks>=35 and marks<60):
    print("Grade D")
elif(marks<35):
    print("fail")
else:
    print("wrong marks inserted plz check!!!")



# switch case - match-case
day=3
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursaday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case _:
        print("invalid day")