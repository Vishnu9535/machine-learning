class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("not a valid name") 
        self.name  =name
        self.house= house
    
    def __str__(self):
        return f"{self.name} is form {self.house}"
    @property
    def house(self): 
        return self.house
    @house.setter
    def house(self,house):
        if not house:
            raise ValueError("not a valid house")
        self.house = house

def main():
    student=get_student()
    # student.h="vrpura"
    print(student)
def get_student():
    # student =Student()
    name=input("Name: ")
    house=input("House: ")
    return Student(name,house)#constucter
if __name__=="__main__":
    main()