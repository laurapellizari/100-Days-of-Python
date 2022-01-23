#Day 02 - Tip Calculator
print("Welcome to the tip calculator.")

total = int(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

pay = (total*(perc/100))/people

print("Each person should pay: $" + pay)