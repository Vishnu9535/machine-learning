exp=str(input("Expression: "))
equ=exp.split(" ")
a=equ[0]
exp=equ[1]
b=equ[-1]

match exp:
    case "+":
        print("{:.1f}".format(int(a)+int(b)))
    case "-":
        print("{:.1f}".format(int(a)-int(b)))
    case "*":
        print("{:.1f}".format(int(a)*int(b)))
    case "/":
        if(b!="0"):
            print("{:.1f}".format(int(a)/int(b)))