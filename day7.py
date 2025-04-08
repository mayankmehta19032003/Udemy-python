import random

word_list = ["ronaldo","mbappe","levandoski"]

random_word = random.choice(word_list)
random_word_length = len(random_word)

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
    ''')




lives =6

for i in range(100):
    print("Word to guess: " + '_' * random_word_length)
    guessed_letter = input("Guess a letter: ")
   
    if guessed_letter in random_word:
        print("Word to guess: " + '_' * random_word_length)
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        lives -= 1
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            print("***********************IT WAS funny! YOU LOSE**********************")
            break
        else:
            print(f"****************************{lives}/6 LIVES LEFT****************************")
