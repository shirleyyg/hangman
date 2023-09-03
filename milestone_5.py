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
        '''
        The check_guess method update the word_guessed list 
        if the letter in the word matches with the letter the user has guessed.
        In the if statement of the method, a for loop has been used to checks 
        if the letter is equal to the guessed letter. 
        Then it replaces the corresponding "_" in the word_guessed with the guessed letter. 
        Then it also decrements the num_letters value.
        '''
        # guess.lower() 
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in range(len(self.word)):
                if letter == guess:
                    self.word_guessed[letter] = guess
            self.num_letters -= 1
        else:
            '''
            In the else statement, the code has been updated to reduces the num_lives by 1 for every incorrect guess. 
            Then it prints out the outstanding num_lives and also inform the user that the letter is not in the word.
            '''
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word: {self.word}. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This method ask for user to guess a letter. Then, it goes through 2 checksc and if the letter passes both checks 
        i.e. not a single alphabetical character and it's not already in the list_of_guesses, 
        then the check_guess method is called in the else block code, 
        passing the guessed letter value and checks if the letter is in the word
        '''
        while True:
            guess = input("Please enter a single letter..")
            if len(guess) != 1 and not guess.isalpha():
                print(f"Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
# player1 = Hangman(['orange', 'banana', 'pear', 'cherry', 'blueberry'])
# player1.ask_for_input()
# print(player1.list_of_guesses)

def play_game(word_list):
    num_lives = 5

    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game.")
            break
    
    print(game.word)

player1 = play_game(['orange', 'banana', 'pear', 'cherry', 'blueberry'])