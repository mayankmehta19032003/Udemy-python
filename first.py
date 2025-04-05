print("Welcome to Pizza shop")

size = input("What size of pizza S , M or L ? ")
pepproni = input("Want pepproni pizza? Y or N: ")
extra_cheese = input("want extra cheese? Y or N: ")
bill =0

if size == "S":
    bill = 15
    if pepproni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if pepproni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else :
    bill = 25
    if pepproni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your total bill is: {bill}")