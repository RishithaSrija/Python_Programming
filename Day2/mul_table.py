# multiplication table
def mul_table(n):
    for i in range(1,11):
        print(n," * ",i," = ",n*i)
num=int(input("Enter n for table"))
mul_table(num)