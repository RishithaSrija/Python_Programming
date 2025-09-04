def sum_digits(n):
    ct=0
    while n>0:
        r=n%10
        ct+=1
        n//=10
    print("No.of digits : ",ct)
num=int(input("Enter value : "))
sum_digits(num)