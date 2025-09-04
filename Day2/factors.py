def factors(n):
    s=0
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")
num=int(input("Enter a number : "))        
factors(num)