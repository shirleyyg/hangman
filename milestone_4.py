import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        # guess.lower() 
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word: {self.word}.")
            for letter in range(len(self.word)):
                if letter == guess:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word: {self.word}. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter..")
            if len(guess) != 1 and not guess.isalpha():
                print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
player1 = Hangman(['orange', 'banana', 'pear', 'cherry', 'blueberry'])
player1.ask_for_input()
print(player1.list_of_guesses)