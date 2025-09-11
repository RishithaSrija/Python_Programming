def divison_exp(n1,n2):
    try:
          result=n1/n2
          print("Result : ",result)
    except :
        print("Error division by zero is not allowed. ")
num1,num2=map(int,input("Enter numbers: ").split()) 
divison_exp(num1,num2)
