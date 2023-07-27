class vault:
    def __init__(self,gallons=0,bolts=0, nuts=0):
        self.gallons=gallons
        self.bolts  =  bolts 
        self.nuts = nuts

    def __str__(self):
        return (f"{self.gallons} ,{self.bolts} , {self.nuts}")
    
    def __add__(self, other):
        galleons=self.gallons+other.gallons
        bolts=self.bolts+other.bolts
        nuts=self.nuts+other.nuts
        return vault(galleons,bolts,nuts)
x=vault(100,4,5)
print(x)     
weelsy=vault(500,5,6)
total =x+weelsy
print(weelsy)
print(total)