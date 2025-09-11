from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    @abstractmethod
    def area(self):
        pass 
class Rectangle(shape):
    def area(self):
        ar=self.length*self.breadth
        print("Area odf rectangle: ",ar)
class Circle(shape):
    def area(self):
        radius=self.length
        ar=3.14*radius**2
        print("Area of circle: ",ar)
l,b=map(int,input("Enter length and breadth / radius value").split())
obj=Rectangle(l,b)
obj.area()
obj1=Circle(l,0)
obj1.area()

