from util.ConnUtil import dbConnection
class RentedCars(dbConnection):
    def ListRentedCars(self):
        try:
            self.open()
            select_str='''select * from Vehicle where status=0'''
            self.stmt.execute(select_str)
            data = self.stmt.fetchall()
            for i in data:
                print(i)
            self.close()
        except Exception as e:
            print(e)
