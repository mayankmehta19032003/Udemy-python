alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''
  ____                              ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   
                                          |_|                    
      ''')

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = ""

    if direction == "encode":
        for letter in text:
            if letter in alphabets:
                index = alphabets.index(letter)
                result += alphabets[(index + shift) % 26]
            else:
                result += letter
        print(f"Here's the encoded result: {result}")
    elif direction == "decode":
        for letter in text:
            if letter in alphabets:
                index = alphabets.index(letter)
                result += alphabets[(index - shift) % 26]
            else:
                result += letter
        print(f"Here's the decoded result: {result}")
    else:
        print("Invalid option. Please choose 'encode' or 'decode'.")

    more = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if more != "yes":
        should_continue = False
        print("Goodbye")

