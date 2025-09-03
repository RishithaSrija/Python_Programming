def sum(p,q):
    c=p+q
    return c
def sub(p,q):
    c=p-q
    return c

def mul(p,q):
    c=p*q
    return c

def div(p,q):
    c=p/q
    return c

def mod(p,q):
    c=p%q
    return c

def operators():
    x=int(input("Enter first value"))
    y=int(input("Enter second value"))
    res=mod(x,y)
    print(f"Remainder value {res}")
operators()