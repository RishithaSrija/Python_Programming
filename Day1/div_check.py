#divisible by 5 and 11 or not
def div_check(n):
    if n%5==0 and n%11==0:
        print("It is divisible")
    else:
        print("Not divisible")
num=int(input(" Enter a number"))
div_check(num)