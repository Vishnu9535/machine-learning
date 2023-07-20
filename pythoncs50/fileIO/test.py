x=input("what is ur name ")

file=open("name.txt","a")
file.write(x)
file.close()