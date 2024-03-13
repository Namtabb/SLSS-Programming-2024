
# Guessing game
# Jason K
# March 4

# import random to access the library to use randint
import random

# creating a function to convert string to int
def str_int(user_input: str):
    return int(user_input)

# create a main function
def main():

    # using ranndint to randomly select a number
    answer = random.randint(1,10)

    # making a starting guess to keep track of number of guesses with while loop
    start_guess = 0

# using a while loop to help increment number of guesses
    while start_guess < 5:
        user_input = str_int(input("Guess the number from 1-10 "))
        
        # increments start guess so that while loop breaks when out of guesses
        start_guess += 1
        
        if(user_input > answer):
            print("Guess is too high, you have ", 5 - start_guess, " guesses left")
        elif(user_input < answer):
            print("Guess is too low, you have ",5 - start_guess, " guesses left" )
        else:
            print(f"{user_input} is correct")
            return
        
    # User breaks out of while loop if they runs out of guesses
    print("You have ran out of guesses")
    print(f"the answer was {answer}")

# calls main function   
main()






