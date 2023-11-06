import unittest
from vehicle import *


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car1 = Car("Toyota", "Camry", "2020")

    def test_is_instance(self):
        self.assertIsInstance(self.car1, Car, "Не является экземпляром Car")

    def test_num_wheels(self):
        self.assertEqual(self.car1.num_wheels, 4,
                         "У экземпляра Car не 4 колеса")

    def test_testdrive_speed(self):
        self.car1.testDrive()
        self.assertEqual(self.car1.speed, 60,
                         "В режиме тест драйва не развивает скорость 60")

    def test_park_speed(self):
        self.car1.testDrive()
        self.car1.park()
        self.assertEqual(self.car1.speed, 0, "Авто не остановилось")


if __name__ == '__main__':
    unittest.main()
