#Day 03 - Treasure Island
#*******************************************************************************
#          |                   |                  |                     |
# _________|________________.=""_;=.______________|_____________________|_______
#|                   |  ,-"_,=""     `"=.|                  |
#|___________________|__"=._o`"-._        `"=.______________|___________________
#          |                `"=._o`"=._      _`"=._                     |
# _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
#|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
# _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
#|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
#|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
#____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
#/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
#____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
#/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
#____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
#/______/______/______/______/______/______/______/______/______/______/_____ /
#*******************************************************************************

print("Welcome to Treasure Island. Your mission is to find the treasure.")
q1 = input("Left or Right?")
if (q1.lower() == 'left'):
    print('Left')
    q2 = input("Swim or Wait?")
    if(q2.lower() == 'wait'):
        print('Wait')
        q3 = input('Which door?')
        if(q3.lower() == 'red'):
            print('Burned by fire. Game Over.')
        elif(q3.lower()  == 'blue'):
            print('Eaten by beasts. Game Over.')
        elif (q3.lower() == 'yellow'):
            print('You Win!')
        else:
            print('Game Over.')
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
