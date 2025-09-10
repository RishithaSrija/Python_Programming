def cout_type_str(st):
    cta=ctd=cts=0
    for i in st:
        if i.isalpha():
            cta+=1
        elif i.isdigit():
            ctd+=1
        else:
            cts+=1
    print("Number alphabets : ",cta)
    print("Number digits : ",ctd)
    print("Number special characters : ",cts)
string=input("Enter string ")
cout_type_str(string)