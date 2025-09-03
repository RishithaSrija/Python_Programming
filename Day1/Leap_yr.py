#function with arguments and with return 
def leap_yr(yr):
    if yr%400==0 and yr%100==0 and yr%4==0 :
        return " Centurian Leap Year"
    elif yr%100!=0 and yr%4==0 :
        return " Leap Year "
    else:
        return " Not a leap year"
    
year=int(input("Enter year : "))
res=leap_yr(year)
print(res)
