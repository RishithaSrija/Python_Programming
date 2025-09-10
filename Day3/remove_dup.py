def remove_dup(l1):
    l1=list(set(l1))   
    return l1   
            
my_list=list(map(int,input("Enter list elements: ").split(",")))
print(remove_dup(my_list))