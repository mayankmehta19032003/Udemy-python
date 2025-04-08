import random

word_list = ["ronaldo", "mbappe", "levandoski"]
random_word = random.choice(word_list)
random_word_length = len(random_word)

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
''')

# Show blank word initially
display = ["_"] * random_word_length
print("Word to guess: " + " ".join(display))

lives = 6
guessed_letters = []

while lives > 0:
    guessed_letter = input("\nGuess a letter: ").lower()

    # Check if already guessed
    if guessed_letter in guessed_letters:
        print(f"You already guessed '{guessed_letter}'!")
        continue
    else:
        guessed_letters.append(guessed_letter)

    correct_guess = False
    for index in range(random_word_length):
        if random_word[index] == guessed_letter:
            display[index] = guessed_letter
            correct_guess = True

    # Show current progress every time
    print("Word to guess: " + " ".join(display))

    if "_" not in display:
        print("\n🎉 You won! Well done!")
        break

    if correct_guess:
        print(f"✅ Good job! {lives}/6 LIVES LEFT")
    else:
        lives -= 1
        print(f"❌ '{guessed_letter}' is not in the word.")
        if lives == 0:
            print("\n💀 GAME OVER! You lost.")
            print(f"The word was: {random_word}")
        else:
            print(f"⚠️ {lives}/6 LIVES LEFT")
