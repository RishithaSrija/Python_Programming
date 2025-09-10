def arm1_n(n):
    print("Armstrong numbers from 1 to n:")
    for i in range(1,n):
        temp=i
        s=0
        r=i%10
        s+=r*r*r
        i//=10
        if temp==s:
            print(temp,end=" ")
num=int(input("Enter value : "))
arm1_n(num)
