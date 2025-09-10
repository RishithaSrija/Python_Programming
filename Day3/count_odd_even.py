def count_odd_even(li):
    cte=0
    cto=0
    for i in range(len(li)):

        if li[i]%2==0:
            cte=cte+1
        else:
            cto=cto+1
    print("Even count: ",cte)
    print("Odd count: ",cto)
my_list=list(map(int,input("Enter list elements: ").split(",")))
count_odd_even(my_list)
