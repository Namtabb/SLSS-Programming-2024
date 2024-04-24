# dictionaries
# 12 april 2024

# Big Ideas:
#   - dictionaries are a data structure
#   - dictionaries map keys to values

# Flashback to lists
person = [
    "john",
    "23 years old",
    "4500 1023 2222 1111"
]

person_dict = {
    "name": "john",
    "age": "23 years old",
    "credit card number": "4500 1023 2222 1111"
}

# Get and print the person's name
print(person[0])
print(person[1]) # age?
print(person[2]) # some numbers?

# call the "key" rather than index number
print(person_dict["name"])

# print the last thing in the list
print(person[-1])
print(person[-2])
# print(person[10]) break

# iterate over the person list
#   - print each value

for value in person_dict:
    print(value, person_dict[value])