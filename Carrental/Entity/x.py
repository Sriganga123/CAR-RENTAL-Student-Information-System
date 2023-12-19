import mysql.connector as sql
class dbConnection:
    def open(self):
        try:
            self.conn = sql.connect(host="localhost", database="Vehicle", user="root", password="sonamona624")
            self.stmt = self.conn.cursor()
            print("Database connected")
        except Exception as E:
            print(f"Database cannot connect: {E}")

    def close(self):
        self.conn.close()


class Vehicle(dbConnection, Exception):
    def __init__(self):
        self.vehicleID = ''
        self.make = ''
        self.model = ''
        self.year = ''
        self.dailyRate = ''
        self.status = ''
        self.passengerCapacity = ''
        self.engineCapacity = ''

    def createVehicle(self):
        try:
            self.open()
            self.stmt.execute('''create table if not exists Vehicle(vehicleID int primary key,
                                make varchar(20), model varchar(30), year int, dailyRate decimal(10,2),
                                status char(1), passengerCapacity int, engineCapacity int) ''')
            self.close()
            print("Table created successfully")
        except Exception as E:
            print(E)


v=Vehicle()
v.createVehicle()