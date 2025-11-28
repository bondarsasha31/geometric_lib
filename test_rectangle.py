import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(7, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_positive(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(5, 5), 25)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(3, 0), 6)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(10, 2), 24)
