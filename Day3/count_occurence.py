def print_occ_pattern(st):
    freq={}
    for ch in st:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for key,value in freq.items():
        print(f"{key}{value}",end="")
string=input("Enter string")
print_occ_pattern(string)
