def print_fact(n):
    i=1
    f=1
    while(i<n+1):
        print(i,"*",end="")
        f=f*i
        i+=1
    print("=",f)
num=int(input("Enter number : "))
print_fact(num)