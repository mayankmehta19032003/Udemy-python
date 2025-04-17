from day13_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

print('''__  ___       __             
        / / / (_)___ _/ /_  ___  _____
       / /_/ / / __ '/ __ \/ _ \/ ___/
      / __  / / /_/ / / / /  __/ /    
     /_/ ///_/\__, /_/ /_/\___/_/     
       / /  /____/_      _____  _____
      / /   / __ \ | /| / / _ \/ ___/
     / /___/ /_/ / |/ |/ /  __/ /    
    /_____/\____/|__/|__/\___/_/ ''')

score =0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
      account_b = random.choice(data)



  print(f"Compare A: {format_data(account_a)}.")

  print(''' 
            _    __    
          | |  / /____
          | | / / ___/
          | |/ (__  ) 
          |___/____(_)''')

  print(f"Against B: {format_data(account_b)}.")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  if is_correct:
      score += 1
      print(f"You are right! Current score: {score}")
  else:
      print(f"Sorry, thats wrong. Final score: {score}.")
      game_should_continue = False





