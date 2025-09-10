#print all negative numbers in a list

def neg_ele(l1):
    for i in range(len(l1)):
        if l1[i]<0:
            print(l1[i])
my_list=list(map(int,input("Enter list elements: ").split(",")))
neg_ele(my_list)














