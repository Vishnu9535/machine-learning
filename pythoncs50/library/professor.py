import random


def main():
    x=get_level()
    generate_integer(x)

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if(level==1 or level == 2 or level == 3):
                return level
            raise Exception
        except Exception:
            pass

def generate_integer(level):
    range=level*10
    

if __name__ == "__main__":
    main()