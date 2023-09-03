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

Firstly we define the variables that are required for the hangman game. 
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

### Installation Instructions

### Usage Instructions

### File Structure

### License information