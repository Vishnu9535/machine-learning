def main():
    time=str(input("what time is it ?"))
    result=convert(time)
    if(result > 7 and result < 8):
        print("breakfast time")
    elif(result > 12 and result < 13):
        print("lunch time")
    elif(result > 18 and result < 19):
        print("dinner time")

def convert(time):
    time=time.split(":")
    x=int(time[0])+int(time[-1])/60
       # print(result)
    return round(x,2)



if __name__ == "__main__":
    main()