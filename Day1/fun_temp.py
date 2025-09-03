#function with arg_list and no return
def fahrnheit_to_Celsius(f):
    cel=(float)((5/9)*(f-32))
    print("Celsius temperature : ",round(cel,2))

fahrnheit=float(input("Enter temperature : "))
fahrnheit_to_Celsius(fahrnheit)