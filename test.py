import pickle
import operator


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


if __name__ == '__main__':
    main()
