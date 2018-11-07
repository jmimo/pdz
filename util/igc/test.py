import unittest
from util.igc import parse, analyze
from datetime import timedelta

class Parser(unittest.TestCase):

    def test_parse(self):
        igc = parse('../../test/igc/2015-07-09-Wispile.igc')
        self.assertEqual('Michael Mimo Moratti', igc.pilot)
        self.assertEqual('GIN Boomerang 9', igc.glider)
        self.assertEqual('Flytec, Connect 1', igc.instrument)

        analyze(igc)

        self.assertEqual(1047, igc.min_gps_altitude)
        self.assertEqual(2827, igc.max_gps_altitude)
        self.assertEqual(978, igc.min_baro_altitude)
        self.assertEqual(2731, igc.max_baro_altitude)
        self.assertEqual(46.43445, igc.min_latitude)
        self.assertEqual(46.486666666666665, igc.max_latitude)
        self.assertEqual(7.282516666666667, igc.min_longitude)
        self.assertEqual(7.3531, igc.max_longitude)

        self.assertEqual(timedelta(hours=0, minutes=57, seconds=47), igc.flight_duration)

    def test_parse_invalid_file(self):
        igc = parse('../../test/igc/Invalid.igc')
        self.assertFalse(igc.valid())

    def test_parse_binary_invalid_file(self):
        igc = parse('../../test/igc/2015-07-09-Wispile.kmz')
        self.assertFalse(igc.valid())

    def test_parse_001(self):
        igc = parse('../../test/igc/150516_Mimo Moratti_01.igc')

    def test_coordinates_as_list(self):
        igc = parse('../../test/igc/2015-07-09-Wispile.igc')
        print(igc.coordinates_as_json())

    def test_xctrack(self):
        igc = parse('../../test/igc/2015-08-07-Fiesch.igc')
        self.assertEqual('Michael Mimo Moratti', igc.pilot)
        self.assertEqual('XCTrack', igc.instrument)
        self.assertEqual('OZONE Delta 2', igc.glider)
