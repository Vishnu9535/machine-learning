item=dict()
while  True:
    try:
        fruits=str(input(""))
        fruits=fruits.upper()
        if(fruits in item):
            item[fruits]=item[fruits]+1
        else:
            item[fruits]=1
    except EOFError:
        break
for i in sorted(item):
        print(item[i],i)