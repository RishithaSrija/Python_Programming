from abc import ABC,abstractmethod

class vehicle:
    def __init__(self, vid, license_plate, owner_name):
        self.vid = vid
        self.__license_plate = license_plate
        self.__owner_name = owner_name
        self.__spot_status = None
       
    def getlicense(self):
        return self.__license_plate
    def setlicence(self,lic_num,name,spot):
        self.__license_plate=lic_num
    def getowner(self):
        return self.__owner_name
    def setowner(self,name):
        self.__owner_name=name
    def getspot(self):
        return self.__spot_status
    def setspot(self,spot):
        self.__spot_status=spot
     
    def display(self):
       
        print(f"Vehicle ID:,{self.vid},Lincense_plate of bike:  ,{self.__license_plate},\nOwner name:  ,{self.__owner_name}")
    
    def calculate_parking_fee(self,hrs):

        raise NotImplementedError("Subclasses must override")


class Bike(vehicle):

    def __init__(self, vid, license_plate, owner_name,helmet_req):
        super().__init__(vid,license_plate,owner_name)
        self.helmet=helmet_req
    def display(self):
        print("Bike Details: ")
        print(f"Lincense_plate of bike:  {self.getlicense()} Owner name:  {self.getowner()} Spot Status:  {self.getspot()} Helmet: {self.helmet}")
    def calculate_parking_fee(self,hrs):
        print("Parking fee for Bike: ₹",end="")
        return 20*hrs

class Car(vehicle):
    
    def __init__(self, vid, license_plate, owner_name,seats):
        super().__init__(vid,license_plate,owner_name)
        self.seats=seats
    def display(self):
        print("Car Details: ")
        print("Lincense_plate of car:  ",self.getlicense(),"\nOwner name:  ",self.getowner(),"\nSpot Status:  ",self.getspot(),"Seats: ",self.seats)
    def  calculate_parking_fee(self,hrs):
        print("Parking fee for Car: ₹",end='')
        return 50*hrs
class SUV(vehicle):

    def __init__(self, vid, license_plate, owner_name,four_wheel):
        super().__init__(vid,license_plate,owner_name)
        self.four_wheel=four_wheel
    def display(self):
        print("SUV Details: ")
        print("Lincense_plate of SUV:  ",self.getlicense(),"\nOwner name:  ",self.getowner(),"\nSpot Status:  ",self.getspot(),"4-Wheel-drive: ",self.four_wheel)
    def  calculate_parking_fee(self,hrs):
        print("Parking fee for SUV: ₹",end='')
        return 70*hrs
class Truck(vehicle):

    def __init__(self, vid, license_plate, owner_name,max_load):
        super().__init__(vid,license_plate,owner_name)
        self.max_load=max_load
    def display(self):
        print("Truck Details: ")
        print("Lincense_plate of truck:  ",self.getlicense(),"\nOwner name:  ",self.getowner(),"\nSpot Status:  ",self.getspot(),"Maximum Load: ",self.max_load)
    def  calculate_parking_fee(self,hrs):
        print("Parking fee for Truck: ₹",end='')
        return 100*hrs


class payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class cashPay(payment):
    def process_payment(self,amount):
        print(f"Paid ₹{amount} in cash")
class cardPay(payment):
    def process_payment(self,amount):
        print(f"Paid ₹{amount} using credit/debit card")
class upiPay(payment):
     def process_payment(self,amount):
        print(f"Paid ₹{amount} using UPI")

#task-2
class parkingSpot:
    def __init__(self,spot_id,size):
        self.spot_id=spot_id
        self.size=size
        self.__vehicle=None
    def assign_vehicle(self,vehicle):
        if self.__vehicle is None:
            self.__vehicle=vehicle
            vehicle.setspot(self.spot_id)
            return True
        return False
    def remove_vehicle(self):
        v=self.__vehicle
        if v:
            self.__vehicle=None
            v.setspot(None)
        return v
    def isEmpty(self):
        return self.__vehicle is None
    def getvehicle(self):
        return self.__vehicle

    def show_status(self):
        if self.__vehicle:
            print(f"Vehicle status:\n Spot: {self.spot_id} ({self.size}):Occupied->{type(self.__vehicle).__name__} ({self.__vehicle.getlicense()})")
        else:
             print(f"Vehicle status:\n Spot: {self.spot_id} ({self.size}):Empty")
         
#task-3 

class parkingLot:
    def __init__(self,name):
        self.name=name
        self.spots=[]

    def add_spot(self,spot):
        self.spots.append(spot)

    def show_spot(self):
        print("\nParking Status: ")
        for s in self.spots:
            s.show_status()

    def park_veh(self,veh):
        size_req={
            Bike:["S","M","L","XL"],
            Car:["M","L","XL"],
            SUV:["L","XL"],
            Truck:["XL"]
        }
        for s in self.spots:
            if s.size in size_req[type(veh)] and s.isEmpty():
                s.assign_vehicle(veh)
                return True
        print("No suitable spot to park the vehicle",type(veh).__name__)
        return False

    def unpark_veh(self,veh,hours,pay_method:payment):
        for s in self.spots:
            if not s.isEmpty() and s.getvehicle()==veh:
                s.remove_vehicle()
                fee=veh.calculate_parking_fee(hours)
                print(f"{type(veh).__name__} ({veh.getlicense()}) removed from parking spot {s.spot_id}")
                print(f"Parking fee Calculated =₹{fee}")
                pay_method.process_payment(fee)
                return
        print("Vehicle not found in lot")


if __name__=="__main__":
    lot=parkingLot("CityMall Parking")
    lot.add_spot(parkingSpot(1,'S'))
    lot.add_spot(parkingSpot(2,'M'))
    lot.add_spot(parkingSpot(3,'S'))
    lot.add_spot(parkingSpot(4,'L'))
    lot.show_spot()
    lot.add_spot(parkingSpot(5,'L'))
    lot.add_spot(parkingSpot(6,'XL'))


    print(f"Parking Lot :{lot.name} Total Spots Added: {len(lot.spots)}")

    bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
    car1 = Car("C201", "TS05CD5678", "Priya", 5)
    suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
    truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

    lot.park_veh(bike1)
    lot.park_veh(car1)
    lot.park_veh(suv1)
    lot.park_veh(truck1)

    lot.show_spot()
    lot.unpark_veh(car1,hours=6,pay_method=upiPay())

    lot.show_spot()

