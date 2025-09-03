#function with no arg_list and with return
def max_val():
    a,b=map(int,input("Enter any two values to compare").split())
    if a>b:
        return a
    else:
        return b
res=max_val()
print(res) 