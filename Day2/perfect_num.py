def per_num(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i 
    if(s==n):
        print("Perfect Number : ",n)
    else:
        print("Not a perfect number : ",n)
n=int(input("Enter a number : "))
per_num(n)


