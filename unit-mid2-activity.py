# Mid 2 activity
# April 8
# Jason kao

# accessing library for random
import random

# literally just int function, but I did not know what to do for parameter
def str_to_int(user_input: str):
    return int(user_input)


# dice roll code
def dice_roll():
    user_input = input("How many times do you want to roll? ")
    
    # Input validation
    while not user_input.isnumeric():
        user_input = input("Sorry, please enter a number.\nHow many times do you want to roll? ")
        
    # Rolling algorithm
    for i in range(str_to_int(user_input)):
        print(random.randint(1,6))  
  
# call function     
dice_roll()