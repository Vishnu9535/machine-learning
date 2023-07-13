from pyfiglet import Figlet
import sys
import argparse
import random
figlet=Figlet()
dif_font=figlet.getFonts()
if len(sys.argv) ==1:
    tex=input('INPUT: ')
    f=random.choice(dif_font)
    figlet.setFont(font=f)
    print(figlet.renderText(tex))
elif len(sys.argv) ==3:
    if '-f' in sys.argv[1:] or '--font' in sys.argv[1:]:
        tex=input('Input: ')
        fn=sys.argv[2]
        print(fn)
        try:
            figlet.setFont(font=fn)
            print(figlet.renderText(tex))
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




