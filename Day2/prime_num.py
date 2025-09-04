def prime_num(n):
    if n==1:
        print("Not a prime")
    ct=0
    for i in range(1,n+1):
        if(n%i==0):
            ct+=1
    if(ct==2):
            print("It is a prime number ")
    else:
            print("Not a prime number ")
num=int(input("Enter value:"))
prime_num(num)