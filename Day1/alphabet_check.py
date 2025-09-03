#to check a character is alphabet or not
def check_alpha(st):
    if(st.isalpha()) :
        print("It is an alphabet character")
    else:
        print("Not an alphabet")
ch=(input("Enter character"))
check_alpha(ch)