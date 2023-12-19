from util.ConnUtil import dbConnection
class CustomersList(dbConnection):
    def ListCustomers(self):
        try:
            self.open()
            select_str='''select * from Customer'''
            self.stmt.execute(select_str)
            data = self.stmt.fetchall()
            for i in data:
                print(i)
            self.close()
        except Exception as e:
            print(e)
