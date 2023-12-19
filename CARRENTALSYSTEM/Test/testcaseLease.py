import unittest
from util.ConnUtil import dbConnection
from dao.CreateLease import LeaseCreate

class TestLeaseCreate(unittest.TestCase):
    def setUp(self):
        self.test_conn = dbConnection()
        self.test_conn.open()
    def testCreateLease(self):
        lease_create_instance = LeaseCreate()
        lease_create_instance.conn = self.test_conn
        lease_create_instance.createLease(100, 14, 47, '2023-01-01', '2023-01-10')
        cursor = self.test_conn.conn.cursor()
        cursor.execute("SELECT * FROM Lease WHERE leaseID = 100")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 14)
        self.assertEqual(result[2], 47)
    def tearDown(self):
        self.test_conn.close()

if __name__ == '__main__':
    unittest.main()



