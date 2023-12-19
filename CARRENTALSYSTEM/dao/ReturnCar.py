from util.ConnUtil import dbConnection
from exception.LeaseNotFoundException import  LeaseNotFoundException
class LeaseFind(dbConnection):
    def returnCar(self,leaseID):
        try:
            self.open()
            select_str='''select * from Lease where leaseID=%s'''
            data=(leaseID,)
            self.stmt.execute(select_str,data)
            lease=self.stmt.fetchone()
            if lease:
                print("Lease Found")
                print(f'Lease ID:{leaseID}')
            else:
                raise LeaseNotFoundException(f'Lease with ID {leaseID} not found')
        except LeaseNotFoundException as e:
            print(f"Error:{e}")
        except Exception as e:
            print(e)
        finally:
            self.close()


