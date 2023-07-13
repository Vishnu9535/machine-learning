import random 
import statistics 
import sys
import cowsay
# coin = random.choice(["heads", "tails"])
# print(coin)

# number=random.randint(1,20)
# print(number)
# cards=["j","k","q","a","1"]
# random.shuffle(cards)
# print(cards)
# print(statistics.mean([100,50]))
# try:
#     print("my name is ",sys.argv[1])
# except IndexError:
#     print("less aregiuments")
# if len(sys.argv) >3:
#     sys.exit("more")
# if len(sys.argv) < 2:
#     sys.exit("less")
# for i in sys.argv[1:]:
#     print(i,end=" ")
# print()
if len(sys.argv) >= 2:
    for i in sys.argv[1:]:
        cowsay.trex("hi "+i)