password = "1234"

for i in range(3):
    guess = input("Enter password: ")

    if guess == password:
        print("Login successful!")
        break
    else:
        print("Wrong password!")

else:
    print("Account locked!")