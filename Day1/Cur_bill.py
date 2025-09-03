# calculate current bill
cno=int(input("Enter Consumer number : "))
cname=input("Enter Consumer name  : ")
pmr,lmr=map(int,input("Enter present and last month readings : ").split())

tot_unit=pmr-lmr 
curr_bill=tot_unit*3.80
print("Current bill details : ")
print("Consumer Number : ",cno,"Customer name : ",cname,"Current Bill generated = ",curr_bill)
