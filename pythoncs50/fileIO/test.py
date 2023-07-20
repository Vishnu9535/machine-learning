# x=input("what is ur name ")

# file=open("name.txt","a")
# file.write(f" {x} \n")
# file.close()
with open("name.txt" , "r") as file :
    # file.write(f"{x} \n") 
    l= file.readlines()

for line in l:
    print(line.rstrip())