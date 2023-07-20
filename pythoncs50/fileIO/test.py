# x=input("what is ur name ")

# file=open("name.txt","a")
# file.write(f" {x} \n")
# file.close()
with open("name.txt") as file :
    # file.write(f"{x} \n") 
    l= file.readlines()
# print(l)
for line in sorted(l):
    print(line.rstrip())