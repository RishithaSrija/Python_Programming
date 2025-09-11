# class vehicle:
       
#     def getlicense(self):
#         return self.__license_plate
#     def setlicence(self,lic_num,name,spot):
#         self.__license_plate=lic_num
#     def getowner(self):
#         return self.__owner_name
#     def setowner(self,name):
#         self.__owner_name=name
#     def getspot(self):
#         return self.__spot_status
#     def setspot(self,spot):
#         self.__spot_status=spot 




# class Bike(vehicle):

#     def gethelmet(self):
#         return self.helmet
#     def sethelmet(self,h):
#         self.helmet=h
#     def display(self):
#         print("Bike Details: ")
#         print("Lincense_plate of bike:  ",self.getlicense(),"\nOwner name:  ",self.getowner,"\nSpot Status:  ",self.getspot)
#     def calculate_parking_fee(hrs):
#         print("Parking fee for Bike: ₹",20*hrs)

# class Car(vehicle):
    
#     def getseats(self):
#         return self.seats
#     def setseats(self,s):
#         self.seats=s
#     def display(self):
#         print("Car Details: ")
#         print("Lincense_plate of car:  ",self.getlicense(),"\nOwner name:  ",self.getowner,"\nSpot Status:  ",self.getspot)
#     def  calculate_parking_fee(hrs):
#         print("Parking fee for Car: ₹",50*hrs)
# class SUV(vehicle):

#     def getfour_wheel(self):
#         return self.four_wheel
#     def setfour_wheel(self,w):
#         self.four_wheel=w
#     def display(self):
#         print("SUV Details: ")
#         print("Lincense_plate of SUV:  ",self.getlicense(),"\nOwner name:  ",self.getowner,"\nSpot Status:  ",self.getspot)
#     def  calculate_parking_fee(hrs):
#         print("Parking fee for SUV: ₹",70*hrs)
# class Truck(vehicle):

#     def getmax_load(self):
#         return self.max_load
#     def setmax_load(self,c):
#         self.max_load=c
#     def display(self):
#         print("Truck Details: ")
#         print("Lincense_plate of truck:  ",self.getlicense(),"\nOwner name:  ",self.getowner,"\nSpot Status:  ",self.getspot)
#     def  calculate_parking_fee(hrs):
#         print("Parking fee for Truck: ₹",100*hrs)

# vehicles=[Bike(),Car(),SUV(),Truck()]
# for v in vehicles:
#     v.display()

# class payment:
#     @abstractmethod
#     def process_payment(self,amount):
#         self.amount=amount

# class cashPay(payment):
#     def process_payment(self,amount):
#         print(f"Paid ₹{amount} in cash")
# class cardPay(payment):
#     def process_payment(self,amount):
#         print(f"Paid ₹{amount} using credit/debit card")
# class upiPay(payment):
#      def process_payment(self,amount):
#         print(f"Paid ₹{amount} using UPI")

# payments = [cashPay(), cardPay(), upiPay()]
# for p in payments:
#     p.pay(1000)




# bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
# car1 = Car("C201", "TS05CD5678", "Priya", 5)
# suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
# truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

# #task-2
# class parkingSpot:
#     def assign_vehicle():
#     def remove_vehicle():
         
# #task-3 

# class parkingLot:
#     def add_spot():
#     def show_spot():
#     def park_veh(veh):
#     def unpark_veh(veh):
# #Payment
