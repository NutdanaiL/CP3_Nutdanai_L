def vatCalculate(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result
num=int(input("Please input totalprice : "))
print(vatCalculate(num))