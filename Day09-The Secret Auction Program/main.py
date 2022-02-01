# Day 09 - The Secret Auction Program

import art as a
from replit import clear
print(a.logo)

def highest_bid (bids):
    high = 0
    for key in bids:
        aux = bids[key]
        if (aux > high):
            high = aux
            person = key.upper()

    return print(f'The winner is {person} with ${high}')


flag_game = False
dic = {}
while not flag_game:
    flag_name = False
    name = input('Whats is your name?\n')
    clear()
    bid = int(input("What's your bid? $"))
    dic[name] = bid
    while not flag_name:
        again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if (again == 'no'):
            flag_game = True
            flag_name = True
            highest_bid(dic)
        elif (again == 'yes'):
            flag_name = True
            clear()
        else:
            print('Unrecognized command')
