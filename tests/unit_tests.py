import unittest
from calculate import calc
from square import area as square_area, perimeter as square_perimeter
from circle import area as circle_area, perimeter as circle_perimeter
import math


class TestSquare(unittest.TestCase):
    def test_area_valid(self):
        self.assertEqual(square_area(4), 16)

    def test_perimeter_valid(self):
        self.assertEqual(square_perimeter(4), 16)


class TestCircle(unittest.TestCase):
    def test_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.27, places=2)

    def test_perimeter_valid(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.85, places=2)


class TestCalc(unittest.TestCase):
    def test_calc_square_area(self):
        self.assertEqual(calc('square', 'area', [4]), 16)

    def test_calc_square_perimeter(self):
        self.assertEqual(calc('square', 'perimeter', [4]), 16)

    def test_calc_circle_area(self):
        self.assertAlmostEqual(calc('circle', 'area', [3]), 28.27, places=2)

    def test_calc_circle_perimeter(self):
        self.assertAlmostEqual(calc('circle', 'perimeter', [3]), 18.85, places=2)

    def test_calc_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc('figure', 'area', [3])

    def test_calc_invalid_function(self):
        with self.assertRaises(ValueError):
            calc('circle', 'volume', [3])

    def test_calc_invalid_size(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [3, 4])

    def test_calc_triangle_not_supported(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [3, 4, 5])


if __name__ == '__main__':
    unittest.main()


