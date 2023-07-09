amt_due=50
while(amt_due > 0):
    print ("Amount Due: ",amt_due)
    coin_inserted=int(input("Insert coin: "))
    if(coin_inserted==25 or coin_inserted == 5 or coin_inserted == 10):
        amt_due=amt_due-coin_inserted
print("Change Owed: ",abs(amt_due))