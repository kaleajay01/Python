# single parameter function
print("single parameter function:-")
def greet():
    print("Welcome to Transflower Learning")
    
greet()

#multiple parameter function
print("\nmultiple parameter function:-")
def student(name, course):
    print("Student name",name,"There course name",course)
student("Ajay","MCA")


#Returning Values
print("\nReturning Values:-")
def add(a,b):
    return a+b
result = add(10,11)
print(result)

#Functions Can Return Values
print("\nFunctions Can Return Values:-")
def square(number):
    return number * number
print(square(11))