x=int(input("Please input velocity (km/h):"))
if x > 1:
    y=int(input("Please input time (h):"))
    if y > 1:
        print(int(x/y),"km/h")
    else:
        print("Value of time should be more than 0 (t>0)")
else:
     print("Value of velocity should be more than 0 (v>0)")