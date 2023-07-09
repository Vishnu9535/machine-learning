name=str(input("enter the name"))
name=name[:1].lower()+name[1:]
result=""
for i in name:
    if(i.isupper()):
        i="_"+i.lower()
    result=result+i
print(result)