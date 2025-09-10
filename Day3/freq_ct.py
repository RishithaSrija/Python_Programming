def freq_ct(l1):
   freq={}
   for num in l1:
      if num in freq:
         freq[num]+=1
      else:
         freq[num]=1
   for key,value in freq.items():      
        print(f"{key } -> {value} times appears ")
    
my_list=list(map(int,input("Enter list elements: ").split(",")))
freq_ct(my_list)