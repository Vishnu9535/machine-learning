import random 

class hat:
    # def __init__(self,name):
    #     self.name=name
    #     self.houses=["blore","varanasi","laknow","vizag"]
    #     self.house=random.choice(self.houses)
    
    
    # def __str__(self):
    #     return (f"{self.name} is from {self.house}")
    houses=["blore","varanasi","laknow","vizag"]
    @classmethod
    def choose_house(cls,name):
        print(f"{name} is in {random.choice(cls.houses)}")

# h=hat("vishnu")
# print(h)
hat.choose_house("vishnu ")