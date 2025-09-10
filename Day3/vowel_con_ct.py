def vowel_const(st):
    ctv=ctc=0
    v='aeiouAEIOU'
    for ch in st:
        if ch.isalpha() and ch in v:
            ctv+=1
        else:
            ctc+=1
    print("Number of vowels: ",ctv)
    print("Number of consonants: ",ctc)
string=input("Enter string ")
vowel_const(string)