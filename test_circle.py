import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(3), 9 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)
