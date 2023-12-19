from util.ConnUtil import dbConnection
class LeaseHistory(dbConnection):
    def listLeaseHistory(self):
        try:
            self.open()
            select_str='''select * from Lease'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
            self.close()
        except Exception as e:
            print(e)
