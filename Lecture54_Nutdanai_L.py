def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculator(price):
    vat = 7
    result = price + (price * vat / 100)
    return result
def priceCalculator(price1,price2):
    result1=price1 + price2
    return result1

if login() == True:
    showMenu()
    if menuSelect() == 1:
        price = int(input("Price (THB) : "))
        print(vatCalculator(price))
    else:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(priceCalculator(price1,price2))
else:
    pass