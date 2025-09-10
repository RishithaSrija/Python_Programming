def lowest_freq(l1):
    freq={}
    for num in l1:
      if num in freq:
         freq[num]+=1
      else:
         freq[num]=1
    print("Highest frequency element: ")
    min_freq=float('inf')
    min_ele=None
    for key,value in freq.items():
        if value<min_freq:   
            min_freq=value
            min_ele=key   
    print(f"{min_ele } : Lowest frequency with {min_freq} times")
my_list=list(map(int,input("Enter list elements: ").split(",")))
lowest_freq(my_list)
