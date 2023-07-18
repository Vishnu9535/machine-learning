import random


def main():
    x=get_level()
    score=generate_integer(x)
    print("Score : ",score)
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
    ran=level*10
    s=10
    for i in range(10):
        a=int(random.randint(0,ran))
        b=int(random.randint(0,ran))
        tries=0
        while True:
            try:
                print(a," + ",b," = ",end="")
                ans=int(input())
                if(ans == (a+b)):
                    break
                else:
                    tries=tries+1
                    if(tries >= 3):
                        s=s-1
                        print(a ," + ",b," = ",(a+b))
                        break
                    print("EEE")
                    raise Exception
            except Exception:
                pass
    return s
        
if __name__ == "__main__":
    main()