import unittest
from util.ConnUtil import dbConnection
from exception.CarNotFoundException import CarNotFoundException
from dao.FindCarByID import CarOperations

class TestCarOperations(unittest.TestCase):
    def setUp(self):
        self.test_conn = dbConnection()
        self.test_conn.open()
    def testFindCarById(self):
        car_operations = CarOperations()
        car_operations.conn = self.test_conn
        with self.assertRaises(CarNotFoundException) as context:
            car_operations.findCarById(999)
        self.assertEqual(str(context.exception), "Car with ID 999 not found.")
    def tearDown(self):
        self.test_conn.close()

if __name__ == '__main__':
    unittest.main()

