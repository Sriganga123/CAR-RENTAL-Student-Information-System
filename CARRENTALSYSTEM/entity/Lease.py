class Lease:
    def __init__(self,leaseID,vehicleID,customerID,startDate,endDate,type):
        self.leaseID=leaseID
        self.vehicleID=vehicleID
        self.customerID=customerID
        self.startDate=startDate
        self.endDate=endDate
        self.type=type
        print(f"Lease ID={self.leaseID} \nVehicle ID={self.vehicleID} \nCustomer ID={self.customerID} \nStart Date={self.startDate} \nEnd Date={self.endDate} \nType={self.type}")

Lease(102,1,23,'23/09/2022','17/11/2023','Monthly')