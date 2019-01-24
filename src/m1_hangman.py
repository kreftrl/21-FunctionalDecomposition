"""
Hangman.

Authors: Robert Kreft and Connor Ozatalar
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

def main():

    setup()
    reset_game()

def get_number_guesses():
    print('You set the DIFFICULTY of the game by setting the number of UNSUCCESSFUL choices you can make before you LOSE the game. The traditional form of Hangman sets this number to 5.')
    return(int(input('How many unsuccessful choices do you want to allow yourself? ')))

def get_secret_word():
    minimum_length=int(input('What MINIMUM length do you want for the secret word? '))
    with open('words.txt') as f:
        f.readline()
        string=f.read()
        words=string.split()
        while True: #check whether the word is big enough
            r = random.randrange(0, len(words))
            if len(words[r])>=minimum_length:
                secret_word=words[r]
                return secret_word

def check_guess(guess,secret_word,guesses,returned_string):
    for k in range(len(secret_word)):
        if secret_word[k]==guess:
            returned_string[k]=secret_word[k]
    for k in range(len(returned_string)): #checks returned string to see if guess is present
        if returned_string[k]==guess:
            print('Good guess! You still have',guesses,'guesses left before you LOSE the game!')
            return returned_string,guesses
    guesses = guesses - 1
    print('Sorry! There are no',guess,'letters in the secret word. You have',guesses,'unsucessful guesses before you lose the game!')
    return returned_string, guesses

def return_returned_string(returned_string):
    string_of_returned_string = ''
    for k in range(len(returned_string)):
        string_of_returned_string= string_of_returned_string+str(returned_string[k])
    return(string_of_returned_string)

def running_game_loop(secret_word,guesses,returned_string):
    while True:
        if guesses==0:
            print('You lose! The secret word was: ',secret_word)
            break
        if return_returned_string(returned_string)==secret_word:
            print('You won the game!')
            break
        guess=input('What letter do you want to try? ')
        returned_from_check_guess=check_guess(guess,secret_word,guesses,returned_string)
        returned_string=returned_from_check_guess[0]
        guesses=returned_from_check_guess[1]
        if guesses>0:
            print(return_returned_string(returned_string))

def reset_game():
    response=input('Play another game? (y/n) ')
    if response=='n':
        print('Thanks for playing Hangman! ')
    if response=='y':
        main()

def setup():
    secret_word = get_secret_word()
    running_game_loop(secret_word, get_number_guesses(), len(secret_word) * ['_ '])

main()

