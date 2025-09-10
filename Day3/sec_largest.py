#second largest element 
def second_largest(list1):
     list1=list(set(list1))
     list1.sort()
     print(list1[-2])
      
      
my_list=list(map(int,input("Enter list elements: ").split(",")))
second_largest(my_list)
