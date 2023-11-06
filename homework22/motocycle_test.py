import unittest
from vehicle import *


class TestMotocycle(unittest.TestCase):

    def setUp(self):
        self.moto1 = Motocycle("Ducatti", "Diavel", "2021")

    def test_num_wheels(self):
        self.assertEqual(
            self.moto1.num_wheels, 2, "У экземпляра Motocycle не 2 колеса")

    def test_testdrive_speed(self):
        self.moto1.testDrive()
        self.assertEqual(self.moto1.speed, 75,
                         "В режиме тест драйва не развивает скорость 75")

    def test_park_speed(self):
        self.moto1.testDrive()
        self.moto1.park()
        self.assertEqual(self.moto1.speed, 0, "Мотоцикл не остановился")


if __name__ == '__main__':
    unittest.main()
