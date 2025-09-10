def del_index(i,list):
    del list[i]
    print(list)
my_list=list(map(int,input("Enter list elements: ").split(",")))
rem=int(input("Enter position to delete: "))
s=len(my_list)
del_index(rem,my_list)
