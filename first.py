print("Welcome to rollercoster")
height = int(input("What is your height?"))

if height > 120 :
    print("You are elibile")
    age = int(input("What is your age? "))
    if age <= 18:
        print("ticket is 7Rs")
    elif 18 < age  < 22:
        print("ticket is 12Rs")
    else :
        print("ticket is 15Rs")    
else :
    print("NO")