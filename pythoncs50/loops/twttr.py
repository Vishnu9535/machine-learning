name=str(input("Input: "))
vovels="aeiouAEIOU"
output=""
for i in name:
    if i not in vovels:
        output=output+i
print(output)