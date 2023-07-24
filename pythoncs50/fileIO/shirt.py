import sys
from PIL import Image
if len(sys.argv) !=3:
    sys.exit("enter a valid number of  agument")
lis=[".jpg",".jpeg",".png"]
if any(sys.argv[1].endswith(i) for i in lis):
    sys.exir("not a valid input")
if any(sys.argv[2].endswith(i) for i in lis):
    sys.exir("not a valid input")
