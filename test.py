import pickle


def main():
    with open('all_igcs.pickle', 'rb') as handle:
        data = pickle.load(handle)

        for igc in data:
            print('{} --> {}'.format(igc.file, igc.pilot))


if __name__ == '__main__':
    main()
