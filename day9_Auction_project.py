import os

print('''
___________
 /          \\
 )_______(
 |"""""""|_.-._,.---------.,_.-._
 |       | | |               | | ''-.
 |       |_| |_             _| |_..-'
 |_______| '-' ''' + "---------" + ''' ' '-'
 )"""""""(
/_________\\
.-------------.
/_______________\\''')


should_continue = True
dic = {}

while should_continue == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    dic[name] = bid

    choice = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    if choice == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif choice == "no":
        maxi = 0
        winner = ""
        for name,bid in dic.items():
            if bid > maxi:
                maxi = bid
                winner = name
        print(f"The winner is {winner} with a bid of {maxi}")
        should_continue = False
    else:
        print("Choice should be in yes or no")
        should_continue = False

