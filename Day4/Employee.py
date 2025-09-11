class Emp:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary 
    def dis_emp(self):
        print("Employee details: ")
        print("Name :",self.name,"\nSalary: ",self.salary)
class Manager(Emp):
     def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept 
     def dis_emp(self):
         super().dis_emp()
         print("Department: ",self.dept)
obj=Manager("Rishi",200000,"CSE")
obj.dis_emp()
obj1=Emp("Sai",400000)
obj1.dis_emp()
