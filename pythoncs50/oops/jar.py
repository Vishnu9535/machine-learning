class Jar:
    def __init__(self, capacity=12):
        if not  capacity > 0:
            raise ValueError("not a valid capasity")
        self.cap = capacity
        self.store=0

    def __str__(self):
        emog= "🍪" * self.store
        return f"{emog}"

    def deposit(self, n):
        if n > self.cap:
            raise BaseException("limit exeeded")
        self.cap=self.cap-n
        self.store = self.store+n
    def withdraw(self, n):
        if n > self.store:
            raise ValueError("not enaugh to withdraw")
        self.store=self.store-n
        self.cap=self.cap+n

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.store
    
obj1=Jar(15)
obj1.deposit(4)
# print(obj1)
obj1.withdraw(3)
print(obj1)

