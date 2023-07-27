from  datetime import datetime
from datetime import date, timedelta
import time
import inflect

class findtime:
    def __init__(self):
        self.ptime=str(date.today())  
        self.ptime=self.ptime.split('-')

    def find_time(self):
        dob=input('Enter your date of birth ')
        try:
            m=datetime.fromisoformat(dob)
            self.dob=dob.split('-')
            # print(self.dob)
            finaldate=  date(int(self.ptime[0]),int(self.ptime[1]),int(self.ptime[2]))- date(int(self.dob[0]),int(self.dob[1]),int(self.dob[2]))
            finaltime=int(finaldate.days)*60*24
            return finaltime
        except Exception:
            print("invalid input of date ")  
                  
    def string_of_time(self,finaltime):
        p=inflect.engine()     
        words=p.number_to_words(finaltime,andword="")
        print(words)

def main():
    ft=findtime()
    finaltime=ft.find_time()
    ft.string_of_time(finaltime)


if __name__ == "__main__":
    main()