class Vehicle:
    def __init__(self,vehicleID,make,model,year,dailyRate,status,passengerCapacity,engineCapacity):
        self.vehicleID=vehicleID
        self.make=make
        self.model=model
        self.year=year
        self.dailyRate=dailyRate
        self.status=status
        self.passengerCapacity=passengerCapacity
        self.engineCapacity=engineCapacity
        print(f'Vehicle ID={self.vehicleID} \nMake={self.make} \nModel={self.model} \nYear={self.year} Daily Rate={self.dailyRate} \nStatus={self.status} \nPassenger Capacity={self.passengerCapacity} \nEngine Capacity={self.engineCapacity}')
v=Vehicle(1,"Toyota","Camry",'2022',50.00,1,4,1450)

