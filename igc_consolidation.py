from util.igc import parse
import pickle
import os
import re


def main():
    igc_files = list()
    path = 'data'
    for file in os.listdir(path):
        match = re.match('^[0-9-]{11}([A-Za-z0-9\.-_].*)[-\(]{2}', file)
        if not match:
            raise Exception('filename could not be matched: {}'.format(file))
        pilot_name = match.group(1).replace('_', ' ')
        if file.endswith('.igc'):
            file_path = '{}/{}'.format(path, file)
            print(file_path)
            igc_files.append(parse(file_path, pilot_name))

    with open('all_igcs.pickle', 'wb') as handle:
        pickle.dump(igc_files, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
