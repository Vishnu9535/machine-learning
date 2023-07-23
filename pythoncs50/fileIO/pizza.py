import csv
import sys
from tabulate import tabulate
table=[]
try: 
    with open(sys.argv[-1]) as file:
        reader=csv.reader(file)
        for x in reader:
            table.append(x)
except FileNotFoundError:
    sys.exit("file does not exist")
print(tabulate(table,headers="firstrow",tablefmt="grid"))