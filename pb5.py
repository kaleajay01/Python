while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator closed")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Answer =", a + b)
    elif choice == 2:
        print("Answer =", a - b)
    elif choice == 3:
        print("Answer =", a * b)
    elif choice == 4:
        print("Answer =", a / b)
    else:
        print("Invalid choice")