def remove_dup(l1):
    ini_len=len(l1)
    l1=list(set(l1))   
    after_len=len(l1)
    diff=ini_len-after_len
    return diff   
            
my_list=list(map(int,input("Enter list elements: ").split(",")))
print("Duplicate count: ",remove_dup(my_list))