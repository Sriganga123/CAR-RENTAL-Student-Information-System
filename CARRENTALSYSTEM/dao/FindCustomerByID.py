from exception.CustomerNotFoundException import CustomerNotFoundException
from util.ConnUtil import dbConnection

class CustomerOperations(dbConnection):
    def findCustomerById(self,customerID):
        try:
            self.open()
            query_str = '''SELECT * FROM Customer WHERE customerID = %s'''
            data = (customerID,)
            self.stmt.execute(query_str, data)
            customer = self.stmt.fetchone()
            if customer:
                print("Customer Found:")
                print("CustomerID:", customer[0])
            else:
                raise CustomerNotFoundException(f"Customer with ID {customerID} not found.")
        except CustomerNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            self.close()




