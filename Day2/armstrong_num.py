def armstrong(n):
    temp=n
    s=0
    while n>0:
        r=n%10
        s+=r*r*r
        n//=10
    if temp==s:
     print("Armstrong: ",s)
    else:
       print("Not an armstrong")
num=int(input("Enter value : "))
armstrong(num)