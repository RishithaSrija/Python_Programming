def search_char(ch,st):
    cto=0
    for char in st:
     if char==ch:
        cto+=1
    print("Occurence of {st}: ",cto)
character=input("Enter character to be searched: ")
string=input("Enter string in which character is to be searched:")
search_char(character,string)