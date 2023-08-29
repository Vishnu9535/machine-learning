

def mulitple():
    x = int(input("exter the number "))
# y = int(input(" enter the rage of multiple "))
    
    for i in range(1,11):
        for j in range(x):
            print(f"{j} x {i}  = {i*j} \t", end ="  ")
        print()
        
def main():
    mulitple()
 
if __name__=="__main__":
    main()

