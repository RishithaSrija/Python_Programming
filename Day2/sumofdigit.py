def sum_digits(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n//=10
    print("Sum of digits : ",s)
num=int(input("Enter value : "))
sum_digits(num)