# functions
# Jason k
# feb 26

# create a function called say_hello
# when you call it, it prints hello

def say_hello():
    print("hello")

# create a function called say_hello_params
# the parameter we pass in is the name of the person that were greeting
    
def say_hello_params(name):
    print(f"Hello {name.capitalize()}")
    
say_hello()
say_hello_params("Jeffrey")

def how_big(num):
    if num<0:
        return "very small"
    if num< 10:
        return "pretty small"
    if num < 100:
        return "big"
    if num < 1000:
        return "pretty big"
    return " very big"

print(how_big(-1))

result = how_big(10000)
print(result)