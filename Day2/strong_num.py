#strong number 145=1!+4!+5!=145
def fact(rem):
    f=1
    for i in range(1,rem+1):
        f=f*i
    return f
def strong_num(n):
    temp=n
    s=0
    while(n>0):
        r=n%10
        s+=fact(r)
        n//=10
    if(temp==s):
        print("Strong number ")
    else:
        print("Not a strong number ") 
num=int(input("Enter a number : "))
strong_num(num)