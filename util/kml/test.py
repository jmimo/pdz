import unittest
from util.igc import parse
from util.kml import Kml


class KmlGenerator(unittest.TestCase):

    def test_track(self):
        igc = parse('../../test/igc/2015-07-09-Wispile.igc')

        kml = Kml()

        for record in igc.b_records:
            kml.add_point(record)
        #kml.create_track('2015-07-09-Wispile.kml')
        kml.create_line_string()

