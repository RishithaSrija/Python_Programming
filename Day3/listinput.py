# list user input
def list_input(n):
    my_list=[]
    for _ in range(n):
        my_list.append(input("Enter value: "))
    print(my_list)
size=int(input("Enter size of the list: "))
list_input(size)