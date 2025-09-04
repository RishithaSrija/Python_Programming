def print_dollar(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==j):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
n=int(input("Enter"))
print_dollar(n)