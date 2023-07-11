item=dict()
while  True:
    fruits=str(input(""))
    fruits=fruits.upper()
    try:
        if(fruits in item):
            item[fruits]=item[fruits]+1
        else:
            item[fruits]=1
    except EOFError:
        for i in sorted(item):
            print(item[i],i)
        break