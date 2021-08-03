cap = 0
lat = 0
esp = 0
iced = 0
ordertype = " "
pricedict = {
    "Cappuccino": 3.00,
    "Espresso": 2.25,
    "Latte": 2.50,
    "Iced Coffee": 2.50
}

while True:
    mode = input("New Order/Daily Summary: ")
    if mode == "New Order":
        order = {
            "Cappuccino": 0,
            "Espresso": 0,
            "Latte": 0,
            "Iced Coffee": 0
        }
        while mode == "New Order":
            items = 0
            while ordertype == " ":
                ordertypechoice = input("Dine in or Take out? ")
                if ordertypechoice == "Dine in":
                    ordertype = ordertypechoice
                elif ordertypechoice == "Take out":
                    ordertype = ordertypechoice
                else:
                    print("Invalid Input")

            while items < 4:
                print("Please order from the following: Cappuccino, Latte, Espresso, Iced Coffee")
                order = input("")
                if order == "Cappuccino":
                    items += 1
                    cap += 1
                    print("Item Added!")
                elif order == "Latte":
                    items += 1
                    lat += 1
                    print("Item Added!")
                elif order == "Espresso":
                    items += 1
                    esp += 1
                    print("Item Added!")
                elif order == "Iced Coffee":
                    items += 1
                    iced += 1
                    print("Item Added!")
                else:
                    print("Invalid Input")
            print("Order Complete")

    elif mode == "Daily Summary":
        print()
    else:
        print("Invalid Input")
