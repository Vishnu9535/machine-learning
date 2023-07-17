import random
while True:
    try:
        num=int(input("Level: "))
        if(num > 0):
            ans=random.randint(1,num)
            try: 
                guess=int(input("Guess: "))
                if(guess > ans):
                    print("Too large")
                if(guess < ans):
                    print("Too small")