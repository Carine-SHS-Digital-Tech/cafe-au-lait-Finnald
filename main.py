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
        orderdict = {
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

            print("Please order from the following; Cappuccino, Latte, Espresso, Iced Coffee: ")
            print("or press enter to end the order. ")
            while items < 4:
                order = input("")
                if order == "Cappuccino":
                    items += 1
                    cap += 1
                    orderdict["Cappuccino"] = cap
                    print("Item Added!")
                elif order == "Latte":
                    items += 1
                    lat += 1
                    orderdict["Latte"] = lat
                    print("Item Added!")
                elif order == "Espresso":
                    items += 1
                    esp += 1
                    orderdict["Espresso"] = esp
                    print("Item Added!")
                elif order == "Iced Coffee":
                    items += 1
                    iced += 1
                    orderdict["Iced Coffee"] = iced
                    print("Item Added!")
                elif order == "":
                    print("Order ended")
                    break
                else:
                    print("Invalid Input")
            print("Confirm the order:")
            for key, value in orderdict.items():
                print(f"{value} {key}")
            confirm = input("Confirm? (Yes/No)")
    elif mode == "Daily Summary":
        print()
    else:
        print("Invalid Input")
