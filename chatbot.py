# Chatbot
# Jaosn K
# March 8
import random
good_possible_resp = ["I'm really happy for you.", "that's really good news.", "thats awesome"]
bad_possible_resp = ["imagine", "sad", "ok"]

# 1. Greets the user
print("hello there")
# 2. Asks them, "how are you?" or something like it
print("How are you doing?")
user_feeling = input().strip(" ,.?1").lower()
# 3. Responds with a general statement
if user_feeling == "good" or user_feeling == "great":
    chosen_response = random.choice(good_possible_resp)
    print(chosen_response)
elif user_feeling == "bad" or user_feeling == "not too good":
    chozen_response = random.choice(bad_possible_resp)
    print(chozen_response)
else:
    print("thanks for sharing that with me")
# 4. Says goodbye 
    print("thank you for your time")