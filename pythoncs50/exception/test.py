# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             return int(input("What's x?"))
#         except :
#             print("x is not an integer")


# main()
try:
    while True:
        line = input("Enter a line of text: ")
        # Process the input
        print("You entered:", line)
except EOFError:
    print("Ctrl+D (EOF) detected. Exiting...")