def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n): 
    print(n % 2)
    return n % 2 == 0
x="ell there"
main()