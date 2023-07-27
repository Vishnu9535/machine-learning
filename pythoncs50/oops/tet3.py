class wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("not a valid name")
        self.name=name
    
class student(wizard):
    def __init__(self,name , house):
        super().__init__(name)
        self.house=house
    def __str__(self):
        return f"{self.name} is from {self.house}"
    

class teacher(wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject
    def __str__(self):
        return f"{self.name} teaches {self.subject}"    
    
wis= wizard("vishnu")
print(student("vishnu","blore"))
print(teacher("vishnu","maths"))
