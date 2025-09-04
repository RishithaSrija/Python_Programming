#sum of first and last digit
def sumof_fandl(n):
    last_d=n%10
    k=0
    while n>10:
        n//=10
    first_d=n
    print("Sum of first and last number",first_d+last_d)
n=int(input("Enter number : "))
sumof_fandl(n)