def prime(m):
    if m<2:
       return False
    for i in range(2,int(m**0.5)+1):
        if(m%i==0):
           return False
    return True
def prime_fact(n):
    for i in range(2,n+1):
        if(n%i==0)and prime(i):
           print(i, end=" ")

num=int(input("Enter a number : "))        
prime_fact(num)
