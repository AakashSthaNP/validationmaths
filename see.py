# Practising 
import random
usrlist = ["aakash","shyam","hari","ram","narayan","krish"]
passlist = ["admin@123","superuser@admin"]

usr = input("Enter Username :  ")


if usr in usrlist:
    print(f"Hello {usr}!!! ")
    passl = input("Enter Password : ")
    if passl in passlist:
        print(f"Welcome {usr} !! to the system!!! ")
        def wel_come():
            # wrong print(f"Thanks By System!! {usrlist[random(0,5)]} !!!")
            pass
        
        print(f"Ths is addition, subtraction, multiplication and division!! System by {usrlist[0]} !! ")
        print("for 2 number enters!! ")
        firstno = int(input("Enter First number -->  "))
        secondno = int(input("Enter Second number -->  "))
        whats = input("What do you want to do A,S,M and D :  ").lower()
        if whats == "a":
            addition = firstno + secondno
            print(addition)
        elif whats == "s":
            subtraction = firstno - secondno
            print(subtraction)
        elif whats == "m":
            multiply = firstno * secondno
            print(multiply)
        elif whats == "d":
            division = firstno / secondno
            print(division)
        else:
            print(f"Sorry!!! {whats} is not available enter a,s,m or m to take answer!!! {usr}!!! ")

        wel_come()
    else:
        print("Password Incorrect!!! ")
else:
    print("Please enter correct username to processed!!! ")