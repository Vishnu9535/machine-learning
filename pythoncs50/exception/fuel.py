

while True:
    x =str(input("fraction "))
    num=x.split("/")
    try:
        num1=int(num[0])
        num2=int(num[-1])
        if(num1 > num2):
            raise Exception
        percent = int((num1/num2)*100)
    except (ValueError, ZeroDivisionError):
        pass
    except Exception:
        pass
    else:
        if(percent <= 1):
            print("E")
        elif(percent >= 99):
            print("F")
        else:
            print(percent,"%")
        break
        
