#Day 05 - Create a Password Generator
import random

letters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-']

poss = letters + numbers + symbols

print('Welcome to the PyPassword Generator!')

size = int(input('How many letters would you like in your password?'))
size_sim = int(input('How many symbols would you like?'))
size_num = int(input('How many numbers would you like?'))

l = 0
n = 0
s = 0
passw = []
for i in range(0, size):
    while (l != size - size_num - size_num):
        while(n != size_num):
            while(s != size_sim):
                passw.append(random.choice(symbols))
                s += 1
            passw.append(random.choice(numbers))
            n += 1
        passw.append(random.choice(letters))
        l += 1

random.shuffle(passw)

password = ''
for j in range(0,len(passw)):
    password = password + passw[j]

print(f'Here is your password: {password}')