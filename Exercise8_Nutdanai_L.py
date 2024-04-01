usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("-----Welcome to DookDik Shop-----")
    print("Please add items that you need into basket")
    print("1. Salmon Oil  390 baht")
    print("2. Spray grooming 290 baht")
    print("3. Dry Shampoo for pets 159 baht")
    userselected = int(input(">> : "))
    if userselected == 1:
        print("1. Salmon Oil  390 baht")
        quantity = int(input("Please input quantity : "))
        price = quantity * 390
        print("Total price:", price, "THB", quantity, "each.")
    elif userselected == 2:
        print("2. Spray grooming 290 baht")
        quantity1 = int(input("Please input quantity : "))
        price1 = quantity1 * 290
        print("Total price:", price1, "THB", quantity1, "each.")
    elif userselected == 3:
        print("3. Dry Shampoo for pets 159 baht")
        quantity2 = int(input("Please input quantity : "))
        price2 = quantity2 * 159
        print("Total price:", price2, "THB", quantity2, "each.")
else:
    print("wrong password !")