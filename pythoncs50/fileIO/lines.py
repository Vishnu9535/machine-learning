import sys
if(len(sys.argv)>2):
    sys.exit("Too many command-line arguments")
elif(len(sys.argv) <2):
    sys.exit("too few arguments")
elif(str(sys.argv[-1]).endswith(".py")):
    try: 
        with open(sys.argv[-1]) as file:
            lines=file.readlines()
            print(len(lines))
    except Exception:
        sys.exit("not file exist")
else:
    print("Not a Python file")
