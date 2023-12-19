from util.ConnUtil import dbConnection
class RemoveCustomer(dbConnection):
    def removeCustomer(self, customerID):
        try:
            self.open()
            delete_str = '''DELETE FROM Customer WHERE customerID = %s'''
            data = (customerID,)
            self.stmt.execute(delete_str, data)
            self.conn.commit()
            self.close()
            print("Customer removed successfully.")
        except Exception as e:
            print(e)


