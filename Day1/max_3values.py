#max of three values
def max_3values(a,b,c):
    if (a>b):
        if(a>c):
            print("Max value : ",a)
        else:
            print("Max value : ",c)
    else:
        if(b>a):
            print("Max value : ",b)
        else:
             print("Max value : ",c)
x,y,z=map(int,input("Enter 3 values : ").split())
max_3values(x,y,z)