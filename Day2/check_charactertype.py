def Check_charactertype(st):
    if (st.isalpha()):
    #if(st [a-z] and st ^[A-Z]):
        print("Alphabet")
    elif(st.isdigit()):
        print("Digit")
    else:
        print("Special Character")
ch=input("Enter character : ")
Check_charactertype(ch)