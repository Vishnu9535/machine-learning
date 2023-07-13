month=[ "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
# pattern1=r'^\w+\s\w+,\s\w+$'
# pattern2=r'^\w+/+\w+/+\w+$'
while True:
    try:
        date=str(input("Date: "))
        if "/" in date:
            udate=date.split("/")
            if len(udate)==3:
                if(int(udate[0]) > 12 or int(udate[1]) >31):
                    raise  Exception
                formatted_date = "-".join([udate[2], udate[0].zfill(2), udate[1].zfill(2)])
                print(formatted_date)
                break
            raise Exception
        else:
            udate=date.split(", ")
            udate1=str(udate[0]).split(" ")
            if int(udate1[1]) >31:
                raise Exception
            m=int(month.index(str(udate1[0])))+1
            print("-".join([udate[-1],str(m).zfill(2),udate1[1].zfill(2)]))
            break
    except Exception:
        pass