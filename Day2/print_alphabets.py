def print_alphabets(st):
    s=97
    while(s<(ord(st)+1)):
        print(chr(s))
        s=s+1
ch=input("Enter a character to print alphabets : ")
print_alphabets(ch)