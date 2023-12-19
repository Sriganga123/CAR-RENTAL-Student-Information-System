import unittest
from util.ConnUtil import dbConnection
from dao.AddCar import ADDCAR

class TestADDCAR(unittest.TestCase):
    def setUp(self):
        self.test_conn = dbConnection()
        self.test_conn.open()
    def testAddCar(self):
        car = ADDCAR()
        car.conn = self.test_conn
        car.addCar(899, 'Toyota', 'Camry', 2022, 50.0, 1, 5, 2.5)
        cursor = self.test_conn.conn.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = 899")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Toyota')
        self.assertEqual(result[2], 'Camry')
    def tearDown(self):
        self.test_conn.close()

if __name__ == '__main__':
    unittest.main()










