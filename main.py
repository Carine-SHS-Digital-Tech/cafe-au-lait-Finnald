cap = 0
lat = 0
esp = 0
iced = 0
pricedict = {
    "Cappuccino": 3.00,
    "Espresso": 2.25,
    "Latte": 2.50,
    "Iced Coffee": 2.50
}

while True:
    mode = input("New Order/Daily Summary: ")
    if mode == "New Order":
        while mode == "New Order":
            print("Please order from the following: Cappuccino, Latte, Espresso, Iced Coffee")
            order1 = input("")
            if order1 == "Cappuccino":
                cap += 1
                print("Item Added!")
            elif order1 == "Latte":
                lat += 1
                print("Item Added!")
            elif order1 == "Espresso":
                esp += 1
                print("Item Added!")
            elif order1 == "Iced Coffee":
                iced += 1
                print("Item Added!")
            else:
                print("Invalid Input")
    elif mode == "Daily Summary":
        print()
    else:
        print("Invalid Input")
