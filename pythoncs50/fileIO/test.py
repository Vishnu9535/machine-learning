# x=input("what is ur name ")

# file=open("name.txt","a")
# file.write(f" {x} \n")
# file.close()
# with open("name.txt") as file :
#     # file.write(f"{x} \n") 
#     l= file.readlines()
# print(l)
# for line in sorted(l):
#     print(line.rstrip())
students=[]
with open("students.csv") as file:
     for line in file:
          name,house=line.rstrip().split(",")
          student={}
          student['name']=name
          student['house']=house 
          students.append(student)


for stu in students:
     print(stu)
     print(f"{stu['name']} is in  {stu['house']}")