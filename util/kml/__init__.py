from collections import namedtuple
from itertools import chain

Point = namedtuple('Point', ['when', 'latitude', 'longitude', 'height'])


def create_line_string(igc):
    kml = Kml()
    for record in igc.b_records:
        kml.add_point(record)
    return kml.create_line_string()


def create_track(igc):
    kml = Kml()
    for record in igc.b_records:
        kml.add_point(record)
    return kml.create_track()


class Kml:

    def __init__(self):
        self.track_points_ = list()

    def add_point(self, b_record):
        self.track_points_.append(Point(b_record.datetime.strftime('%Y-%m-%dT%H:%M:%SZ'), b_record.point.latitude, b_record.point.longitude, b_record.gps_altitude))

    def create_line_string(self):
        kml = self.header()
        kml = chain(kml, self.linestring_generator())
        kml = chain(kml, self.footer())
        return kml

    def create_track(self):
        kml = self.header()
        kml = chain(kml, self.track_generator())
        kml = chain(kml, self.footer())
        return kml

    def save_as_file(self, kml, file_name):
        file = open(file_name, 'w')
        for line in kml:
            file.write(line + '\n')
        file.close()

    def track_generator(self):
        yield '<Placemark>'
        yield '<name>My Track</name>'
        yield '<styleUrl>#track_h</styleUrl>'
        yield '<gx:Track>'
        yield '<altitudeMode>absolute</altitudeMode>'
        for track_point in self.track_points_:
            yield '<when>{}</when>'.format(track_point.when)
            yield '<gx:coord>{} {} {}</gx:coord>'.format(track_point.longitude, track_point.latitude,
                                                         track_point.height)
        yield '</gx:Track>'
        yield '</Placemark>'

    def linestring_generator(self):
        yield '<Placemark>'
        yield '<name>My Flight</name>'
        yield '<styleUrl>#track_h</styleUrl>'
        yield '<LineString>'
        yield '<altitudeMode>absolute</altitudeMode>'
        yield '<coordinates>'
        for track_point in self.track_points_:
            yield '{},{},{} '.format(track_point.longitude, track_point.latitude, track_point.height)
        yield '</coordinates>'
        yield '</LineString>'
        yield '</Placemark>'

    def point_generator(self, point):
        yield '<Placemark>'
        yield '<Timestamp><when>{}</when></Timestamp>'.format(self.format_timestamp(point.date, point.record.time))
        yield '<Point><coordinates>{},{}</coordinates></Point>'.format(point.record.longitude, point.record.latitude)
        yield '</Placemark>'

    def header(self):
        yield '<?xml version="1.0" encoding="UTF-8"?>'
        yield '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" ' \
              'xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">'
        yield '<Document>'

        yield '<Style id="track_h">'
        yield '<IconStyle>'
        yield '<scale>1.2</scale>'
        yield '<Icon>'
        yield '<href>http://earth.google.com/images/kml-icons/track-directional/track-none.png</href>'
        yield '</Icon>'
        yield '</IconStyle>'
        yield '<LineStyle>'
        yield '<color>FF0080FF</color>'
        yield '<width>3</width>'
        yield '</LineStyle>'
        yield '</Style>'

    def footer(self):
        yield '</Document>'
        yield '</kml>'
