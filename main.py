running = 1
cap = 0
lat = 0
esp = 0
iced = 0
while running == 1:
    mode = input("New Order/Daily Summary: ")
    while mode == "New Order":
        print("Please order from the following: Cappuccino, Latte, Espresso, Iced Coffee")
        order1 = input("")
        order = []
        if order1 == "Cappuccino":
            cap = cap + 1
            print("Item Added!")
        elif order1 == "Latte":
            lat = lat + 1
            print("Item Added!")
        elif order1 == "Espresso":
            esp = esp + 1
            print("Item Added!")
        elif order1 == "Iced Coffee":
            iced = iced + 1
            print("Item Added!")
        else:
            print("Invalid Input")
