import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(10), 100)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(7), 28)
