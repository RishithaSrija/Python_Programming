def palindrome_bw(n):
    for i in range(1,n+1):
        if(str(i)==str(i)[::-1]):
            print(i,end=" ")
    
num=int(input("Enter a number :"))
palindrome_bw(num) 