def note_count(n):
    temp=n
    ct_500=n//500
    if(n>=500):        
        print(f"500 rupee notes:{ct_500}")
    rem_amt=ct_500%500
    ct_200=rem_amt//200
    if(rem_amt>=200):       
        print(f"200 rupee notes:{ct_200}")
    rem_amt=ct_200%20
    ct_100=rem_amt//100
    if(rem_amt>=100):
        print(f"100 rupee notes:{ct_100}")
    rem_amt=ct_100%100
    # if(rem_amt>=20):
    #     ct_20=n//20
    #     print(f"20 rupee notes:{ct_20}")
    # rem_amt=ct_20%20
    # if(rem_amt>=10):
    #     ct_10=n//10
    #     print(f"200 rupee notes:{ct_10}")
    # rem_amt=ct_10%10

amt=int(input("Enter your amount : "))
note_count(amt)