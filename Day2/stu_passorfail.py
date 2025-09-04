# student details display total ,average of student and details check his/her grades
def stu_p_f(avg):
 if(avg>=40):
    print("Pass")
    if(avg<50):
      print("Grade C")
    elif(avg<=70 and avg>50):
       print("Grade B")
    elif(avg<=80 and avg>70):
       print("Grade A")
    elif(avg>80):
       print("Passed with Distension")
 else:
   print("Fail")

stu_num=int(input("Enter Student roll number : "))
stu_name=input("Enter Student name : ")
sub1,sub2,sub3=map(int,input("Enter 3 subject marks : ").split())
tot_marks=sub1+sub2+sub3
avg=(float)(tot_marks/3)

print(f"Student Details : \nStudent number : {stu_num } \n Student name : {stu_name} \n Total marks : {tot_marks} \n Average of Student : {round(avg,2)}")
stu_p_f(avg)