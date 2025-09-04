# calculate current bill based on units

def curbill_units(tot):
    if (tot in range(0,51)):
        cost=(50*3.80)
        return cost
    elif (tot in range(51,101)):
        cost=(50*3.80)+(tot-50)*4.20
        return cost
    elif(tot in range(100,201)):
        cost=(50*3.80)+(50)*4.20+(tot-100)*5.10
        return cost
    elif(tot in range(200,301)):
        cost=(50*3.80)+(50)*4.20+(100)*5.10+(tot-150)*6.30
        return cost
    elif(tot>300):
        cost=(50*3.80)+(50)*4.20+(100)*5.10+(100)*6.30+(tot-300)*7.50
        return cost

cno=int(input("Enter Consumer number : "))
cname=input("Enter Consumer name  : ")
pmr,lmr=map(int,input("Enter present and last month readings : ").split())

tot_unit=pmr-lmr 
curr_bill=curbill_units(tot_unit)
print("Current bill details : ")
print("Consumer Number : ",cno,"Customer name : ",cname,"Current Bill generated = ",curr_bill)
