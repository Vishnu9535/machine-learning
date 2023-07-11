menu=dict()
menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# order="Tortilla Salad"
# print(menu[order])
cost=0
while True:
    
    try:
        order=str(input("Item: "))
        order=order.title()
        cost=cost+float(menu[order])
        print("${:.2f}".format(cost))
    except Exception:
        pass
    except KeyboardInterrupt:
        break