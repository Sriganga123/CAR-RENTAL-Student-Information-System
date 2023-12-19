from util.ConnUtil import dbConnection
class ADDCAR(dbConnection):
    def addCar(self, vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity):
        try:
            data = [(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity)]
            create_str = '''INSERT INTO Vehicle(vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''

            self.open()
            self.stmt.executemany(create_str, data)
            self.conn.commit()
            self.close()

            print("Inserted Successfully")
        except Exception as e:
            print(e)


