def string_len(s1,s2):
    ct1=0
    ct2=0
    for _ in s1:
        ct1+=1
    print("Length of the String :",ct1)
    for _ in s2:
        ct2+=1
    print("Length of the String :",ct2)
    if  ct1>ct2:
        print(s1+s2)
    elif ct2>ct1:
        print(s2+s1)
     

st1=input("Enter a string1: ")
st2=input("Enter string2: ")
length=string_len(st1,st2)
