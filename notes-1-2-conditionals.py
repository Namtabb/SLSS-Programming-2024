# Conditionals
# Author: Jason
# 14 Feb 2024

# Implement the flowchart from the notes

# Create two variables, x and y
x = 1_000_000
y = -5.2

# If x is less than y, print that
if x < y: 
    print("x is less than y")

# If x is greater than y, print that
if x > y:
    print("x is greater than y")

# If x is equal, print that
if x == y:
    print("x is equal to y")


if x < y :
    print("x is less than y")
elif x > y :
    print("x is greater than y")
elif x == y :
    print("x is equal to y")

# ask user what thei fav fruit is
    
fave_fruit = input("whats your favourite fruit?")

# ask user for age

user_age = input("how old are you")

if fave_fruit == "apple" or fave_fruit == "orange" :
    print("delicious choice")

# if they answer banana and are 2 years old
    
if fave_fruit == "banana" and user_age == "2" :
    print("banas are delicious")

    #