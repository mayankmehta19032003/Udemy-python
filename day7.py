import random

word_list = ["mouse","alt","lenovokawasaki"]

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
                   |___/''')

print("Word to guess: " + '_' * random_word_length)



for i in range(1,7):
    guessed_letter = input("Guess a letter: ")

    if guessed_letter in random_word:
        print("****************************6/6 LIVES LEFT****************************")
        print("Word to guess: " + '_' * random_word_length)
    else:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        print(f"****************************6/6 LIVES LEFT****************************")
