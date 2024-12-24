# Program to calculate the year when the user will turn 100 years old

# Asking for user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculating the current year
from datetime import datetime
current_year = datetime.now().year

# Calculating the year when the user will turn 100
year_turn_100 = current_year + (100 - age)

# Displaying the result
print(f"\nHello {name}!")
print(f"You are {age} years old.")
print(f"You will turn hundered years old in the year {year_turn_100}.")
