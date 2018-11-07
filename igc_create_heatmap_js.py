import pickle
import operator
import simplekml
import util.geo


def main():
    with open('all_igcs.pickle', 'rb') as handle:
        data = pickle.load(handle)

        all_points = list()

        for igc in data:
            all_points.extend([record.point for record in igc.b_records])

        with open('mapdata.js', 'w') as js:
            for point in all_points:
                js.write('new google.maps.LatLng({}, {}),\n'.format(point.latitude, point.longitude))


if __name__ == '__main__':
    main()
