import csv
import sys
with open ("before.csv") as file:
    reader=csv.DictReader(file)
    with open("after.csv","w") as file2:
        fn=["first_name","last_name","house"]
        writer=csv.writer(file2)
        writer.writerow(fn)
        writer=csv.DictWriter(file2,fieldnames=fn)
        for x in reader:
            first_name,last_name=x['name'].split(', ')
            writer.writerow({"first_name":first_name,"last_name":last_name,"house":x['house']})