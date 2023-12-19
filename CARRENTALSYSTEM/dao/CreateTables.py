import mysql.connector as sql
from util.ConnUtil import dbConnection
class TableCreation(dbConnection):
    def CreateTables(self):
        try:
            self.open()
            self.stmt.execute('''create table if not exists Vehicle(vehicleID int primary key,
                                make varchar(30),
                                model varchar(30),
                                year varchar(5),
                                dailyRate float,
                                status int,
                                passengerCapacity int,
                                engineCapacity int)''')
            print("Vehicle Table created")
            self.stmt.execute('''create table if not exists Customer(customerID int primary key,
                            firstName varchar(30),
                            lastName varchar(30),
                            email varchar(30),
                            phoneNumber char(10))''')
            print("Customer Table created")
            self.stmt.execute('''create table if not exists Lease(leaseID int primary key,
                            vehicleID int,
                            customerID int,
                            startDate varchar(30),
                            endDate varchar(30),
                            FOREIGN KEY(vehicleID) REFERENCES Vehicle(vehicleID),
                            FOREIGN KEY(customerID) REFERENCES Customer(customerID))''')
            print("Lease table created")
            self.stmt.execute('''create table if not exists Payment(paymentID int primary key,
                            leaseID int,
                            paymentDate varchar(30),
                            amount float,
                            FOREIGN KEY(leaseID) references Lease(leaseID))''')
            print("Payment table created")
            self.close()
        except Exception as e:
            print(e)
tab=TableCreation()
tab.CreateTables()
