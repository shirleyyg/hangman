'''
Hangman is a classic game in which a player thinks of a word 
and the other player tries to guess that word within a certain amount of attempts. 
This is an implementation of the Hangman game, where the computer thinks of a word 
and the user tries to guess it.
'''
import random

word_list = ['orange', 'banana', 'pear', 'cherry', 'blueberry']

word = random.choice(word_list)


user_input = input("Please enter a single letter..")
if len(user_input) == 1 and user_input.isalpha():
    guess = user_input
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print(word_list)
print(word)
# print(guess)