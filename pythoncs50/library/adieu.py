import inflect 
import sys
# p=inflect.engine()
# animal="lion"
# print("I saw", N, p.plural_noun(animal, N))
# print("I saw ", p.no(animal))
# errors=0
# print(p.plural_adj("has"))
names=[]
while True:
    try:
        x=str(input("Name: "))
        names.append(x)
    except EOFError:
        break
x=len(names)-1
result="Adieu, adieu, to "
if x==1:
    result=result+names[x]
else:
    for arg in names[:x]:
        result=result+arg+", "
    result=result+"and "+names[x]
print(result)