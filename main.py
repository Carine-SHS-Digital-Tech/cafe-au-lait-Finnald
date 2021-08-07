#initialises variables
import csv
captotal = 0
lattotal = 0
esptotal = 0
icedtotal = 0
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

while True:     #never turns off unless break
    mode = input("New Order/Daily Summary: ").lower()
    if mode.lower() == "new order":
        orderdict = {}      #empty dictionary for later
        ordertype = " "
        items = 0
        cap = 0
        lat = 0
        esp = 0
        iced = 0
        while mode == "new order":          #asks for the order type
            while ordertype == " ":
                ordertypechoice = input("Dine In or Take Out? ")
                if ordertypechoice.lower() == "dine in":
                    ordertype = ordertypechoice
                    dine += 1
                    charge = 0
                elif ordertypechoice.lower() == "take out":
                    ordertype = ordertypechoice
                    take += 1
                    charge = 0.05
                else:
                    print("Invalid Input")

            print("Please order from the following; Cappuccino, Latte, Espresso, Iced Coffee: ")        #building the customer's order
            print("or press enter to end the order. ")
            while True:            #order loop
                order = input("")
                if order.lower() == "cappuccino":       #adds the coffee type to an empty dictionary to make the sales receipt an appropriate size
                    quant = int(input("How many? "))
                    cap += quant
                    captotal += quant
                    orderdict["Cappuccino"] = cap
                    print("Item Added!")
                elif order.lower() == "latte":
                    quant = int(input("How many? "))
                    lat += quant
                    lattotal += quant
                    orderdict["Latte"] = lat
                    print("Item Added!")
                elif order.lower() == "espresso":
                    quant = int(input("How many? "))
                    esptotal += quant
                    esp += quant
                    orderdict["Espresso"] = esp
                    print("Item Added!")
                elif order.lower() == "iced coffee":
                    quant = int(input("How many? "))
                    icedtotal += quant
                    iced += quant
                    orderdict["Iced Coffee"] = iced
                    print("Item Added!")
                elif order == "":
                    print("Order ended")
                    break                       #if the customer decides they want to end their order, leaves the order loop
                else:
                    print("Invalid Input")      #if an irrelevant value is entered, lets the user try again
            print("Confirm the order:")
            for key, value in orderdict.items():
                print(f"{value} {key}")                 #prints all the items in the order for confirmation
            confirm = " "
            while confirm == " ":
                confirmchoice = input("Confirm order? (Yes/No) ")   #confirms the order
                if confirmchoice.lower() == "yes":
                    totalorders += 1
                    confirm = confirmchoice
                    gtotal = 0
                    print("Sales receipt: ")
                    print("{:<15} {:<10} {:<20} {:<20} {:<10} {:<15} {:<10}".format("Item", "Quantity", "Single Item Price", "Price Excl. GST", "GST", "Extra Charges", "Total"))   #headers for sales receipt
                    for key, value in orderdict.items():        #prints the sales receipt in tabular format
                        print("{:<15} {:<10} {:<20} {:<20} {:<10} {:<15} {:<10}".format(key, value, pricedict[key], value*pricedict[key], round(value*pricedict[key]*0.1, 2), round((value*0.1+value*pricedict[key])*charge,2), round((value*pricedict[key]+value*pricedict[key]*0.1+(value*0.1+value*pricedict[key])*charge), 2)))
                        gtotal += round(value*pricedict[key]+value*pricedict[key]*0.1+(value*pricedict[key]+value*pricedict[key]*0.1)*charge, 2)
                        #               |    og amount     |        gst              |                      extra charge                    |
                    totalinc += gtotal
                    print(f"Grand Total: ${round(gtotal, 2)}")
                    tender = ""
                    while tender == "":     #asks for amount tendered to calculate change
                        while True:
                            try:            #only lets the user proceed by entering a float value and doesnt break the program
                                tendered = float(input("Amount tendered ($): "))
                                break
                            except:
                                print("Invalid Input")
                        if isinstance(tendered, float):     #checks if the amount tendered is a float and then only calculates change if the amount tendered is the same or more than the grand total
                            if tendered >= gtotal:
                                print(f"Change: ${round(tendered-gtotal, 2)}")
                                tender = tendered
                            elif tendered < gtotal:
                                print("Insufficient funds") #if the amount tendered is less than the grand total, the customer needs more money
                        else:
                            print("Invalid Input")
                    re = input("Print receipt? (Yes/No) ")  #this is the part where the employee asks the customer if they want a receipt
                    if re.lower() == "yes":
                        print("Receipt printed")
                    else:
                        print()
                elif confirmchoice.lower() == "no":
                    break
                else:
                    print("Invalid Input")
            mode = " "      #resets the mode for selection

    elif mode.lower() == "daily summary":       #prints daily summary contents in a tabular format
        print("{:<15} {:<15}".format("Menu Item", "Frequency"))
        print("{:<15} {:<15}".format("Cappuccino", captotal))
        print("{:<15} {:<15}".format("Espresso", esptotal))
        print("{:<15} {:<15}".format("Latte", lattotal))
        print("{:<15} {:<15}".format("Iced Coffee", icedtotal))
        print()
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Dine in Freq.", "Take out Freq.", "Total Orders", "Total Cups", "Total Income", "Total GST"))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(dine, take, totalorders, captotal+esptotal+lattotal+icedtotal, round(totalinc, 2), round(totalinc/1.1*0.1, 2)))

        with open("daily_orders.csv", "w", encoding="UTF8", newline="") as f:   #writes the values to daily_orders.csv
            writer = csv.writer(f)
            data = [                        #is the values to be written to daily_orders.csv
                ["Menu Item", "Frequency"],
                ["Cappuccino", captotal],
                ["Espresso", esptotal],
                ["Latte", lattotal],
                ["Iced Coffee", icedtotal],
                [""],
                ["Dine in Freq.", "Take out Freq.", "Total Orders", "Total Cups", "Total Income", "Total GST"],
                [dine, take, totalorders, captotal+esptotal+lattotal+icedtotal, round(totalinc, 2), round(totalinc/1.1*0.1, 2)]
            ]
            writer.writerows(data) #writes to csv
    else:
        print("Invalid Input")
