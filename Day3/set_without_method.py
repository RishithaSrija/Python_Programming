def add_set(val,s):
    s.add(val)
    print("Added to set")
def remove_set(val,s):
    s.discard(val)
    print("Value discarded ")
def set_ope(a,b):
    print("Union: ",a|b)
    print("Intersection: ",a&b)
    print("difference: ",a-b)
    print("Symmetric difference: ",a^b)

def set_usage():
    myset=set()
    add_set(787,myset)
    add_set(78,myset)
    add_set(87,myset)
    remove_set(78,myset)
    print(myset)
    seta={1,2,3,4,5}
    setb={4,5,6,7}
    set_ope(seta,setb)
set_usage()