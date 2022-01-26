import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lists = [rock, paper, scissors]

print('Welcome to the Rock Paper Scissors game')
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(lists[user_choice])
print('Computer chose: ')
pc_choice = random.randint(0,2)
print(lists[pc_choice])

if(user_choice == pc_choice):
    print('Its a draw')
elif(user_choice == 0) and (pc_choice == 2):
    print('You win!')
elif(user_choice == 1) and (pc_choice == 0):
    print('You win!')
elif(user_choice == 2) and (pc_choice == 1):
    print('You win!')
else:
    print('You lose')