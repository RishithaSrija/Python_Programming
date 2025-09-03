# simple interest and total amount in hand 
p=int(input("Enter principle amount : "))
t=int(input("Enter time period(in months) : "))
r=int(input("Enter rate of interest : "))
si_it=(p*t*r)//100

print("Simple Interest calculated : ",si_it)
tot_amt=p+si_it
print("Total amount in hand  : ",tot_amt)

