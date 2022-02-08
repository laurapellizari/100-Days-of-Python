# Day 12 - The Number Guessing Game

import art
import random

def sort_number():
    number = random.randint(0,100)
    return number

def play(number, dif):
    if (dif == 'easy'):
        guess = 10
    elif (dif == 'hard'):
        guess = 5

    while guess != 0:
        print(f'You have {guess} attempts remaining to guess the number')
        choose = int(input('Make a guess: '))
        if (choose > number):
            guess -= 1
            print('Too high.\nGuess again.')
        elif (choose < number):
            guess -= 1
            print('Too low.\nGuess again.')
        elif (choose == number):
            print(f'You got it! The answer was {number}')
            guess = 0


def game():
    print(art.logo)
    print('Welcome to the Number Guessing Game!')
    flag_on = True
    while flag_on:
        print("I'm thinking of a number between 1 and 100.")
        dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
        flag_wrong = True
        while flag_wrong:
            if (dif == 'easy') or (dif == 'hard'):
                flag_wrong = False
            else:
                print('Command not recognized.')
                dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
        number = sort_number()
        play(number, dif)


game()