x=input("what is ur name ")

file=open("name.txt","a")
file.write(f" {x} \n")
file.close()