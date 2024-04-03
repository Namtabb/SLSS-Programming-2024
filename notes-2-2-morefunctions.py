# More functions
# April 3 2024
# Jason

#implement stars functions

def stars(num):
    """Returns specify number for stars"""
    value = "" #placeholder for return value

    #if number is 0, return 1 star
    # if number is 1, return 1 star
    # elif number is greater than 1, retur that num * star
     #else return error saying negative nums aren't allowed
    if num == 0 or num == 1:
        value = "*"
    elif num > 1:
        value = "*" * num
    else:
        value = "sorry, can't take negative numbers."

    return value
    



# multiply strings
# greeting = " hello"
# print(greeting * 3)

# print(" the quick brown fox jumps over the lazy dog" * 2)

print(stars(2))

