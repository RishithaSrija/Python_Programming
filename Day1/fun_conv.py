#function with no arg_list and no return
def conversion():
    kilo_mt=int(input("Enter kilometers : "))
    #b=int(input("Enter b value : "))
    miles=0.62*kilo_mt
    print("Kilometers to miles : ",round(miles,2))
conversion()