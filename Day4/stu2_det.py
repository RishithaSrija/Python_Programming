class student_2:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Student Details:")
        print("Student name: ",self.name,"\nStudent marks: ",self.marks)
s1=student_2("Rvai",56)
s1.display()
s2=student_2("Sai",78)
s2.display()