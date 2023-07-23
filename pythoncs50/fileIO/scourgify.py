import csv
import sys
if(len(sys.argv) > 3):
    sys.exit("too many arguments")
elif(len(sys.argv) < 3):
    sys.exit("too few arguments")

try:
    with open (sys.argv[1]) as file:
        reader=csv.DictReader(file)
        with open(sys.argv[2],"w") as file2:
            fn=["first_name","last_name","house"]
            writer=csv.writer(file2)
            writer.writerow(fn)
            writer=csv.DictWriter(file2,fieldnames=fn)
            for x in reader:
                first_name,last_name=x['name'].split(', ')
                writer.writerow({"first_name":first_name,"last_name":last_name,"house":x['house']})
except FileNotFoundError:
    sys.exit("could not read "+sys.argv[1])