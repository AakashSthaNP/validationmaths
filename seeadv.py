import random

usrlist = ["aakash", "shyam", "hari", "ram", "narayan", "krish"]
passlist = ["admin@123", "superuser@admin"]

usr = input("Enter Username: ")

if usr in usrlist:
    print(f"Hello {usr}!!!")
    passl = input("Enter Password: ")
    if passl in passlist:
        print(f"Welcome {usr} to the system!!!")

        def wel_come():
            print(f"Thanks from System!! {random.choice(usrlist)} !!!")

        print(f"This is an Addition, Subtraction, Multiplication, and Division System by {usrlist[0]}!!")
        print("Enter two numbers!")

        try:
            firstno = int(input("Enter First Number --> "))
            secondno = int(input("Enter Second Number --> "))
        except ValueError:
            print("Invalid number entered. Exiting program!")
            exit()

        whats = input("What do you want to do - A (Add), S (Subtract), M (Multiply), D (Divide): ").lower()
        if whats == "a":
            print("Addition Result:", firstno + secondno)
        elif whats == "s":
            print("Subtraction Result:", firstno - secondno)
        elif whats == "m":
            print("Multiplication Result:", firstno * secondno)
        elif whats == "d":
            if secondno != 0:
                print("Division Result:", firstno / secondno)
            else:
                print("Cannot divide by zero!")
        else:
            print(f"Sorry!!! {whats} is not available. Enter 'a', 's', 'm', or 'd'!!! {usr}!!! ")

        wel_come()
    else:
        print("Password Incorrect!!!")
else:
    print("Please enter correct username to proceed!!!")
