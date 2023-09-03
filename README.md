# Hangman

## Table of Contents

1. Introduction
2. Installation Instructions
3. Usage Instructions
4. File Structure
5. License information

### Introduction

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Instructions:
Firstly, we need to create a new repo fro the project in Github and clone it to local folder using git clone and repor url via Terminal

Firstly a new python script file called milestone_2.py is created. Here we define the variables that are required for the hangman game. 
Following are the required variables:
1. word_list = A list of strings such as fruits
2. word = selects a string from the list randomly
3. guess = user input to guess a letter

Then we create 2 functions:
1. check_guess 
This function checks whether the guessed letter is in the randomly selected word

2. ask_for_input
    1. This function uses while loop to iteratively check if the input is a valid guess and breask out of the loop if it passes the check i.e. if it is a single alphabetical character.
    2. Then it calls the check_guess method to check if this letter is in the word

Note: After every changes or updates in the local repository, we need to update GitHub repository with the latest code changes. Firstly, staging your modifications (using command git add .) and creating a commit (using command git commit -m 'description'). Then, pushed the changes to GitHub repository (using command git push).

Next step is to create a class for the game. For this new python script file called milestone_4.py is created.
In the class, the above 2 functions have been used and updated to make the game more robust.
The ask_for_input has been updated to add another check if the user's guessed letter is already in list_of_guesses using if elif statements.
If the letter passes both checks i.e. not a single alphabetical character and it's not already in the list_of_guesses, then the check_guess method is called in the else block code, passing the guessed letter value and checks if the letter is in the word

The check_guess method has been updated to update the word_guessed list if the letter in the word matches with the letter the user has guessed.
In the if statement of the method, a for loop has been used to checks if the letter is equal to the guessed letter. Then it replaces the corresponding "_" in the word_guessed with the guessed letter. Then it also decrements the num_letters value.

In the else statement, the code has been updated to reduct the num_lives by 1 for every incorrect guess. Then it prints out the outstanding num_lives and also inform the user that the letter is not in the word.

### Installation Instructions

### Usage Instructions

### File Structure

### License information