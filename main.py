capTotal = 0
latTotal = 0
espTotal = 0
icedTotal = 0
dine = 0
take = 0
totalinc = 0
totalorders = 0
pricedict = {
    "Cappuccino": 3.00,
    "Espresso": 2.25,
    "Latte": 2.50,
    "Iced Coffee": 2.50
}

while True:
    mode = input("New Order/Daily Summary: ")
    if mode == "New Order":
        orderdict = {}
        ordertype = " "
        items = 0
        cap = 0
        lat = 0
        esp = 0
        iced = 0
        while mode == "New Order":
            while ordertype == " ":
                ordertypechoice = input("Dine in or Take out? ")
                if ordertypechoice == "Dine in":
                    ordertype = ordertypechoice
                    dine += 1
                    charge = 0
                elif ordertypechoice == "Take out":
                    ordertype = ordertypechoice
                    take += 1
                    charge = 0.05
                else:
                    print("Invalid Input")

            print("Please order from the following; Cappuccino, Latte, Espresso, Iced Coffee: ")
            print("or press enter to end the order. ")
            while items < 4:
                order = input("")
                if order == "Cappuccino":
                    items += 1
                    cap += 1
                    capTotal += 1
                    orderdict["Cappuccino"] = cap
                    print("Item Added!")
                elif order == "Latte":
                    items += 1
                    lat += 1
                    latTotal += 1
                    orderdict["Latte"] = lat
                    print("Item Added!")
                elif order == "Espresso":
                    items += 1
                    espTotal += 1
                    esp += 1
                    orderdict["Espresso"] = esp
                    print("Item Added!")
                elif order == "Iced Coffee":
                    items += 1
                    icedTotal += 1
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
            confirm = " "
            while confirm == " ":
                confirmchoice = input("Confirm order? (Yes/No) ")
                if confirmchoice == "Yes":
                    totalorders += 1
                    confirm = confirmchoice
                    gtotal = 0
                    print("{:<15} {:<10} {:<20} {:<20} {:<10} {:<15} {:<10}".format("Item", "Quantity", "Single Item Price", "Price Excl. GST", "GST", "Extra Charges", "Total"))
                    for key, value in orderdict.items():
                        print("{:<15} {:<10} {:<20} {:<20} {:<10} {:<15} {:<10}".format(key, value, pricedict[key], value*pricedict[key], round(value*pricedict[key]*0.1, 2), round((value*0.1+value*pricedict[key])*charge,2), round((value*pricedict[key]+value*pricedict[key]*0.1+(value*0.1+value*pricedict[key])*charge), 2)))
                        gtotal += round(value*pricedict[key]+value*pricedict[key]*0.1+(value*0.1+value*pricedict[key])*charge, 2)
                        totalinc += gtotal
                    print(f"Grand Total: {round(gtotal, 2)}")
                    re = input("Print receipt? (Yes/No) ")
                    if re == "Yes":
                        print("Receipt printed")
                    else:
                        print()
                else:
                    print("Invalid Input")
            mode = " "

    elif mode == "Daily Summary":
        print("{:<15} {:<15}".format("Menu Item", "Frequency"))
        print("{:<15} {:<15}".format("Cappuccino", capTotal))
        print("{:<15} {:<15}".format("Espresso", espTotal))
        print("{:<15} {:<15}".format("Latte", latTotal))
        print("{:<15} {:<15}".format("Iced Coffee", icedTotal))
        print()
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Dine in Freq.", "Take out Freq.", "Total Orders", "Total Cups", "Total Income", "Total GST"))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(dine, take, totalorders, capTotal+espTotal+latTotal+icedTotal, round(totalinc, 2), round(totalinc/1.1*0.1, 2)))
    else:
        print("Invalid Input")
