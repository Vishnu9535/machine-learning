# Get the user's input
# x = 6.1
# y = 85000.5

# # Create a rounded result
# z = round(x + y)

# # Print the formatted result
# print(f"{z:,}")
# squares = list(map(lambda x: x**2, range(10)))
# print(squares.length())
# x=input("write something")
# print(x.strip())
# name = input("What's your name? ")

# Remove whitespace from the str
# name = name.strip()

# # Print the output
# print(f"hello, {name}")
# print(name.title())
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")