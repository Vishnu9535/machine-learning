import csv 
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
# with open("students.csv") as file:
#      for line in file:
#           name,house=line.rstrip().split(",")
#           student={}
#           # student['name']=name
#           # student['house']=house 
#           students.append({"name":name,"house":house})
with open("students.csv") as file:
     # reader =csv.reader(file)
     reader =csv.DictReader(file)
     print(reader)
     for row in reader:
          print(row)
          students.append({"name":row["name"],"house":row["home"]})
          print(students)


for stu in sorted(students,key=lambda x:x["name"]):
     print(f"{stu['name']} is from  {stu['house']}")

     