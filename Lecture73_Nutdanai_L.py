systemMenu = {"ข้าวมันไก่":40, "ข้าวหมกไก่":45, "ข้าวขาหมู":40, "ข้าวปลาทอด":60}
menuList=[]

def showBill():
    Total = 0
    print("")
    print("My Foods".center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        Total += int(menuList[number][1])
    print("Total of price : %d" %(Total))
    print("")

print("ข้าวมันไก่ (40), ข้าวหมกไก่ (45), ข้าวขาหมู (40), ข้าวปลาทอด (60)")
while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
      menuList.append([menuName,systemMenu[menuName]])

showBill()
