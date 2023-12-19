from util.ConnUtil import dbConnection
class LeaseCreate(dbConnection):
    def createLease(self,leaseID,vehicleID,customerID,startDate,endDate):
        try:
            create_str='''INSERT INTO Lease(leaseID,vehicleID,customerID,startDate,endDate) values(%s,%s,%s,%s,%s)'''
            data=[(leaseID,vehicleID,customerID,startDate,endDate)]
            self.open()
            self.stmt.executemany(create_str,data)
            self.conn.commit()
            self.close()
            print("Inserted Successfully")
        except Exception as e:
            print(e)



