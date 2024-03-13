# Methods - string Methods
# Author Jason K
# 21 feb 2024

# Ask the user what the weather is
user_reply = input("what is the weather like?")

#if they answer rainy, say
# bring an umbrella
if user_reply.strip(" !.?,").lower()== "rainy":
    print("bring an umbrella")
else:
    print("sorry i didnt understand what you said")