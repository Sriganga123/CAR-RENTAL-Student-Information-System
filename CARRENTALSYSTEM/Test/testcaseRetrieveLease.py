import unittest
from util.ConnUtil import dbConnection
from dao.ListLeaseHistory import LeaseHistory

class TestLeaseHistory(unittest.TestCase):
    def setUp(self):
        self.test_conn = dbConnection()
        self.test_conn.open()
    def testListLeaseHistory(self):
        lease = LeaseHistory()
        lease.conn = self.test_conn
        lease.listLeaseHistory()
    def tearDown(self):
        self.test_conn.close()

if __name__ == '__main__':
    unittest.main()
