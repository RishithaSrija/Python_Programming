def print_sum(n):
    i=1
    while(i<n+1):
        print(i,"+",end="")
        i+=1
    sum=n*(n+1)//2
    print("=",sum)


num=int(input("Enter n value for natural numbers sum"))
print_sum(num)
