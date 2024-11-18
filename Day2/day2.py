# Day 2 Features a small calculator project
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? Choose 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = (bill + (bill * (tip / 100)))/ people
print(f"Each person should pay: {total: .2f}")

