def note_count(n):
    print(f"Amount: {n}")
    notes=[500,200,100,50,20,10,5,1]
    for note in notes:
        ct=n//note
        if ct>0:
            print(f"{note } rupee notes:{ct}")
            n=n%note

amt=int(input("Enter your amount : "))
note_count(amt)
