class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("not a valid name") 
        self.name  =name
        self.house= house
    
    def __str__(self):
        return f"{self.name} is form {self.house}"
    @property #getter 
    def house(self): 
        return self._house
    @house.setter
    def house(self,house):
        if not house:
            raise ValueError("not a valid house")
        self._house = house
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("not a valid name")
        self._name=name
    @classmethod
    def get_student(cls):
    # student =Student()
        name=input("Name: ")
        house=input("House: ")
        return cls(name,house)
def main():
    student=Student.get_student()
    # student._house="vishnu "
    print(student)

    # return Student(name,house)#constucter
if __name__=="__main__":
    main()