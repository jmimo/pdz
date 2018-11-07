import pickle
import operator
import simplekml
import util.geo


def main():
    with open('all_igcs.pickle', 'rb') as handle:
        data = pickle.load(handle)

        pilots = dict()

        for igc in data:
            if igc.pilot in pilots:
                pilots[igc.pilot] += 1
            else:
                pilots[igc.pilot] = 1
            print('{} --> {}'.format(igc.file, igc.pilot))

        for pilot, amount in sorted(pilots.items(), key=operator.itemgetter(1), reverse=True):
            print('{} = {}'.format(pilot, amount))

        kml = simplekml.Kml()
        kml.document.name = 'PDZ_2018'

        for igc in data:
            points = [record.point for record in igc.b_records]
            createTrack(kml, igc.pilot, points)

        kml.savekmz('all_tracks.kmz', format=False)


def createTrack(kml, pilot, points):
    track = kml.newlinestring(name=pilot)
    coordinates = list()
    for index, point in enumerate(points[1:]):
        if index % 5 == 0:
            coordinates.append([point.longitude, point.latitude, point.altitude])
    track.coords = coordinates


if __name__ == '__main__':
    main()
