# student details display total ,average of student and details
stu_num=int(input("Enter Student roll number : "))
stu_name=input("Enter Student name : ")
sub1,sub2,sub3=map(int,input("Enter 3 subject marks : ").split())
tot_marks=sub1+sub2+sub3
avg=(float)(tot_marks/3)

print(f"Student Details : \n Student number : {stu_num } Student name : {stu_name} Total marks : {tot_marks} Average of Student : {round(avg,2)}")