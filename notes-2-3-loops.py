# lopps and iteration
# april 5
# Jason

for _ in range(2):
    print("something")


grocery_list = [
    "1"
    "2"
    "3"
]

for item in grocery_list:
    print("----")
    print(f"* {item}")
    if item == 1:
        break


for i in range(10):
    # modulo
    if i%2 == 0:
        print(f"{i} is an even number")


counter = 0

while counter < 10:
    print(counter)

    if counter % 2 == 0:
        print(f"{counter} is an even number")
    else:
        print(counter)

    counter += 1