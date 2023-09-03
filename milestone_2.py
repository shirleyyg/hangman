import random

word_list = ['orange', 'banana', 'pear', 'cherry', 'blueberry']
word = random.choice(word_list)

def check_guess(guess):
    # guess.lower() 
    if guess.lower() in word:
        print(f"Good guess! {guess} is in the word: {word}.")
    else:
        print(f"Sorry, {guess} is not in the word: {word}. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter..")
        if len(guess) == 1 and guess.isalpha():
            print(f"Good guess! You guessed letter {guess}")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

player1 = ask_for_input()