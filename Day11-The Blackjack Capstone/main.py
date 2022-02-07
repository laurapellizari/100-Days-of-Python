# Day 11 - The Blackjack Capstone Project

import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
flag_off = False

def game_play ():
    print(art.logo)
    your_cards = []
    comp_cards = []
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    sum_cards = sum(your_cards)
    sum_comp = sum(comp_cards)
    if(sum_cards == 21):
        print(f'    Your cards: {your_cards}, current score: {sum_cards}, Blackjack!')
        print(f"    Computer's first card: [{comp_cards[0]}]")
    else:
        print(f'    Your cards: {your_cards}, current score: {sum_cards}')
        print(f"    Computer's first card: [{comp_cards[0]}]")

    flag_again = False

    while not flag_again:
        again = input("Type 'y' to get another card, type 'n' to pass: ")
        if(again == 'n'):
            flag_again = True
            while (sum_comp < 17):
                comp_cards.append(random.choice(cards))
                sum_comp = sum(comp_cards)
            if (comp_cards == sum_comp):
                print("Draw 🙃")
            if(sum_cards > sum_comp) or (sum_comp > 21):
                print(f'    Your cards: {your_cards}, final score: {sum_cards}')
                print(f"    Computer's cards: {comp_cards}, final score {sum_comp}")
                print(('You win!'))
            else:
                print(f'    Your cards: {your_cards}, final score: {sum_cards}')
                print(f"    Computer's cards: {comp_cards}, final score {sum_comp}")
                print(('You lose.'))
        elif(again == 'y'):
            your_cards.append(random.choice(cards))
            sum_cards = sum(your_cards)
            your_cards, comp_cards = check_as(your_cards, comp_cards)
            if(sum_cards > 21):
                print(f'    Your final hand: {your_cards}, final score: {sum_cards}')
                print(f"    Computer's final hand: {comp_cards}, final score {sum_comp}")
                print('You went over. You lose.')
                flag_again = True
            elif (sum_cards == 21):
                print(f'    Your final hand: {your_cards}, final score: {sum_cards}, Blackjack')
                print(f"    Computer's final hand: {comp_cards}, final score {sum_comp}")
                print(('You win!'))
                flag_again = True
            elif (comp_cards == sum_comp):
                print("Draw 🙃")
            else:
                print(f'    Your cards: {your_cards}, current score: {sum_cards}')
                print(f"    Computer's first card: [{comp_cards[0]}]")
        else:
            print('Command not recognized.\n')

def check_as(your_cards, comp_cards):
    for cards in range(0, len(your_cards)):
        if (cards == 11) and (sum(your_cards) > 17):
            your_cards[cards] = 1
    for cards in range(0, len(comp_cards)):
        if (cards == 11) and (sum(comp_cards) > 17):
            comp_cards[cards] = 1
    return your_cards, comp_cards

while not flag_off:
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")
    if(game == 'n'):
        flag_off = True
        print('GoodBye')
    elif(game == 'y'):
        game_play()
    else:
        print('Command not recognized.\n')
