from day13_data import data

print('''__  ___       __             
        / / / (_)___ _/ /_  ___  _____
       / /_/ / / __ '/ __ \/ _ \/ ___/
      / __  / / /_/ / / / /  __/ /    
     /_/ ///_/\__, /_/ /_/\___/_/     
       / /  /____/_      _____  _____
      / /   / __ \ | /| / / _ \/ ___/
     / /___/ /_/ / |/ |/ /  __/ /    
    /_____/\____/|__/|__/\___/_/ ''')

print(f"Compare A: {data[0]['name']}, {data[0]['description']}, {data[0]['country']} ")

print(''' 
          _    __    
         | |  / /____
         | | / / ___/
         | |/ (__  ) 
         |___/____(_)''')

print(f"Against B: {data[1]['name']}, {data[1]['description']}, {data[1]['country']}")

choice = input("Who has more followers? Type 'A' or 'B': ")


