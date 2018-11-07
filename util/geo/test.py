import unittest
from util.igc import Wgs84Point
from util.geo import distance, bearing_rad


class TestFaiDistanceCalculation(unittest.TestCase):

    def test_example(self):
        result = distance(Wgs84Point(46.30440, 8.04091), Wgs84Point(46.56138, 8.33753))
        self.assertAlmostEqual(36513.0, result, delta=0.9)


class Bearing(unittest.TestCase):

    def test_example(self):
        result = bearing_rad(Wgs84Point(46.30440, 8.04091), Wgs84Point(46.56138, 8.33753))
        self.assertAlmostEqual(0.6701, result, places=4)

        result = bearing_rad(Wgs84Point(46.928876, 8.339587), Wgs84Point(46.945041, 8.427873))
        self.assertAlmostEqual(1.30824, result, places=4)

if __name__ == '__main__':
    unittest.main()
