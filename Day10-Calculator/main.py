# Day 10 - Calculator

import art as a

#Functions
def sum (a,b):
    return a + b
def sub (a,b):
    return a - b
def div (a,b):
    return a / b
def mult (a,b):
    return a * b

#Operations
operations = {
    "+": sum,
    "-": sub,
    "/": div,
    "*": mult
}

def calculator ():
    print(a.logo)
    flag_off = False
    flag_again = True
    while not flag_off:
        if(flag_again):
            num1 = int(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)
        op = input('Pick an operation: ')
        num2 = int(input("What's the next number?: "))
        call = operations[op]
        result = call(num1, num2)
        print(f'{num1} {op} {num2} = {result}')
        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")
        flag_again = True
        if (again == 'y'):
            num1 = result
            flag_again = False


calculator()