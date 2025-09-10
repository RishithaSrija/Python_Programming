def highest_freq(l1):
    freq={}
    for num in l1:
      if num in freq:
         freq[num]+=1
      else:
         freq[num]=1
    print("Highest frequency element: ")
    max_freq=0
    max_ele=None
    for key,value in freq.items():
        if value>max_freq:   
            max_freq=value
            max_ele=key   
    print(f"{max_ele } : Highest frequency with {max_freq} times")
my_list=list(map(int,input("Enter list elements: ").split(",")))
highest_freq(my_list)
