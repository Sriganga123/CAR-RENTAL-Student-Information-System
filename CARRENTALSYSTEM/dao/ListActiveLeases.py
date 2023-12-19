from exception.LeaseNotFoundException import LeaseNotFoundException
from util.ConnUtil import dbConnection
from datetime import datetime
class ActiveLease(dbConnection):
    def listActiveLeases(self):
        try:
            self.open()
            current_date = datetime.now().strftime('%Y-%m-%d')
            query_str = '''SELECT * FROM Lease 
                           WHERE startDate <= %s AND endDate >= %s'''
            data = (current_date, current_date)
            self.stmt.execute(query_str, data)
            active_leases = self.stmt.fetchall()
            if active_leases:
                print("List of Active Leases:")
                for lease in active_leases:
                    print("Lease ID:", lease[0])
                    print("Vehicle ID:", lease[1])
                    print("Customer ID:", lease[2])
                    print("Start Date:", lease[3])
                    print("End Date:", lease[4])
                    print("\n")
            else:
                print("No active leases found.")
        except LeaseNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            self.close()

