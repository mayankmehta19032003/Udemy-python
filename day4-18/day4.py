import random

# friends = ["Mayank","Ajay","Sumit","PK"]

# random_index = random.randint(0,3)

# print(friends[random_index])

# arr1= ["A","B","C"]
# arr2= ["D","E","F"]

# arr3 = [arr1,arr2]

# print(arr3[1][1])
# #E

player_choice = int(input("What do you chosse? Type 0 for rock , 1 for scissors and 2 for paper\n"))
computer_choice = random.randint(0,2)

print("Player choice: ",player_choice)
print("Computer choice: ",computer_choice)

if player_choice == computer_choice:
    print("Its draw")

if player_choice == 0 and computer_choice == 1:
    print("You win")
elif player_choice == 0 and computer_choice == 2:
    print("You loose")
elif player_choice == 1 and computer_choice == 0:
    print("You loose")
elif player_choice == 1 and computer_choice == 2:
    print("You Win")
elif player_choice == 2 and computer_choice == 0:
    print("You Win")
elif player_choice == 2 and computer_choice == 1:
    print("You loose")