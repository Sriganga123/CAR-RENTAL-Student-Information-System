from util.ConnUtil import dbConnection
class RemoveCar(dbConnection):
    def removeCar(self, vehicleID):
        try:
            self.open()
            delete_str = '''DELETE FROM Vehicle WHERE vehicleID = %s'''
            data = (vehicleID,)
            self.stmt.execute(delete_str, data)
            self.conn.commit()
            self.close()
            print("Car removed successfully.")
        except Exception as e:
            print(e)


