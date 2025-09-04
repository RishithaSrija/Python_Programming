def prime(m):
    if m==1:
       pass
    ct=0
    for i in range(1,m+1):
        if(m%i==0):
            ct+=1
    if(ct==2):
           return m
    else:
            pass
def prime_fact(n):
    s=0
    for i in range(1,n+1):
        if(n%i==0):
           val=prime(i)
           print(val, end=" ")

num=int(input("Enter a number : "))        
prime_fact(num)