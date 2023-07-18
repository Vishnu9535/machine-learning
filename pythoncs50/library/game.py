import random
while True:
    try:
        num=int(input("Level: "))
        if(num > 0):
            break
        else:
             raise Exception
    except ValueError:
        pass
ans=int(random.randint(1,num))
while True:  
        try: 
            guess=int(input("Guess: "))
            if(guess > ans):
                print("Too large")
                raise Exception 
            elif(guess < ans):
                print("Too small")
            elif(guess == ans):
                 print("Just right")
                 break
        except Exception as e:
                pass