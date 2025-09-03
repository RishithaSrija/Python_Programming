#to check it is positive or negative
def check_pos_neg(n):
    if n>0:
        print("Positive")
    elif n<0:
        print("Negative")
    else:
        print("It is neither positive nor negative",n)
num=int(input("Enter a number"))
check_pos_neg(num)