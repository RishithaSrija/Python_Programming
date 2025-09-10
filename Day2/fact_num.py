def print_fact(n):
    i=1
    f=1
    for i in range(1,n+1):
        f*=i
        if i<n:
            print(i,"*",end="")
        else:
            print(i,end="")
    print("=",f)
num=int(input("Enter number : "))
print_fact(num)
