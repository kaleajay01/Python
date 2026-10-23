num = [12,13,14,11]
maximum = num[0]
for num1 in num:
    if num1 > maximum:
        maximum = num1
print("max number is:",maximum)

# def maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# result = maximum(num1, num2, num3)

# print("Maximum number is:", result)