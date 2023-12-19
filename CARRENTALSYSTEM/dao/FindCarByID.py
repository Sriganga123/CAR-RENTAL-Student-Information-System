from exception.CarNotFoundException import CarNotFoundException
from util.ConnUtil import dbConnection
class CarOperations(dbConnection):
    def findCarById(self, vehicleID):
        try:
            self.open()
            query_str = '''SELECT * FROM Vehicle WHERE vehicleID = %s'''
            data = (vehicleID,)
            self.stmt.execute(query_str, data)
            car = self.stmt.fetchone()
            if car:
                print("Car Found:")
                print("VehicleID:", car[0])
            else:
                raise CarNotFoundException(f"Car with ID {vehicleID} not found.")
        except CarNotFoundException as e:
            print(f"Error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            self.close()




