def unique_ele(l1):
    freq={}
    for num in l1:
      if num in freq:
         freq[num]+=1
      else:
         freq[num]=1
    print("Unique elements: ")
    for key,value in freq.items():
        if freq[key]==1:      
            print(f"{key } ")
my_list=list(map(int,input("Enter list elements: ").split(",")))
unique_ele(my_list)