from exception.LeaseNotFoundException import *
from exception.CustomerNotFoundException import *
from exception.CarNotFoundException import *
from dao.AddCar import ADDCAR
from dao.removeCar import RemoveCar
from dao.ListAvailableCars import AvailableCars
from dao.ListRentedCars import RentedCars
from dao.FindCarByID import CarOperations
from dao.AddCustomer import ADDCUSTOMER
from dao.RemoveCustomer import RemoveCustomer
from dao.ListCustomers import CustomersList
from dao.FindCustomerByID import CustomerOperations
from dao.CreateLease import LeaseCreate
from dao.ReturnCar import LeaseFind
from dao.ListActiveLeases import ActiveLease
from dao.ListLeaseHistory import LeaseHistory
from dao.PaymentRecord import PaymentRecord
if __name__ == '__main__':
    try:
        print("List of Applications:")
        print("1.Add Car \n2.Remove Car \n3.List Available Cars \n4.List Rented Cars \n5.Find Car by ID \n6.Add customer \n"
            "7.Remove Customer \n8.List Customers \n9.Find Customer by ID \n10.Create Lease \n11.Return Car \n12.List Active Leases"
            "\n13.List Lease History \n14.Record Payment")
        print("................................................................................................")
        print("List of Categories:")
        print("1.CAR MANAGEMENT \n2.CUSTOMER MANAGEMENT \n3.LEASE MANAGEMENT \n4.PAYMENT MANAGEMENT")
        print("................................................................................................")
        while True:
            print("1.CAR MANAGEMENT \n2.CUSTOMER MANAGEMENT \n3.LEASE MANAGEMENT \n4.PAYMENT MANAGEMENT \n5.STOP")
            choice=int(input("Enter your choice:"))
            if choice==1:
                print("CAR MANAGEMENT")
                print("1.Add Car \n2.Remove Car \n3.List Available Cars \n4.List Rented Cars \n5.Find Car by ID \n6.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    c = ADDCAR()
                    c.addCar(
                            vehicleID=int(input("Vehicle ID: ")),
                            make=input("Make: "),
                            model=input("Model: "),
                            year=input("Year: "),
                            dailyRate=input("Daily Rate: "),
                            status=int(input("Status: ")),
                            passengerCapacity=int(input("Passenger Capacity: ")),
                            engineCapacity=int(input("Engine Capacity: "))
                            )
                if s==2:
                    r = RemoveCar()
                    r.removeCar(vehicleID=int(input("Enter car ID to remove: ")))
                if s==3:
                    c1 = AvailableCars()
                    c1.ListAvailableCars()
                if s==4:
                    c2 = RentedCars()
                    c2.ListRentedCars()
                if s==5:
                    c3 = CarOperations()
                    c3.findCarById(vehicleID=int(input("Enter car ID to find: ")))
                if s==6:
                    break
            if choice==2:
                print("CUSTOMER MANAGEMENT")
                print("1.Add Customer \n2.Remove Customer \n3.List Customers \n4.Find Customer By ID \n5.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    m = ADDCUSTOMER()
                    m.addCustomer(
                        customerID=int(input("CustomerID:")),
                        firstName=input("First Name"),
                        lastName=input("Last Name"),
                        email=input("Email"),
                        phoneNumber=input("Phone Number")
                    )
                if s==2:
                    m1 = RemoveCustomer()
                    m1.removeCustomer(customerID=int(input("Enter customer ID to remove: ")))
                if s==3:
                    m2 = CustomersList()
                    m2.ListCustomers()
                if s==4:
                    m3 = CustomerOperations()
                    m3.findCustomerById(customerID=int(input("Enter customer ID to find: ")))
                if s==5:
                    break
            if choice==3:
                print("LEASE MANAGEMENT")
                print("1.Create Lease \n2.Return Car \n3.List Active Leases \n4.List Lease History \n5.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    l = LeaseCreate()
                    l.createLease(
                        leaseID=int(input("Lease ID:")),
                        vehicleID=int(input("Vehicle ID")),
                        customerID=int(input("Customer ID")),
                        startDate=input("Start Date"),
                        endDate=input("End Date")
                    )
                if s==2:
                    l1 = LeaseFind()
                    l1.returnCar(leaseID=int(input("Lease ID:")))
                if s==3:
                    l2 = ActiveLease()
                    l2.listActiveLeases()
                if s==4:
                    l3 = LeaseHistory()
                    l3.listLeaseHistory()
                if s==5:
                    break
            if choice==4:
                print("PAYMENT MANAGEMENT")
                print("1.Record Payment \n2.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    p = PaymentRecord()
                    p.recordPayment()
                if s==2:
                    break
            if choice==5:
                break
    except CarNotFoundException as e:
        print(e)
    except CustomerNotFoundException as e:
        print(e)
    except LeaseNotFoundException as e:
        print(e)
    except Exception as e:
        print(e)
