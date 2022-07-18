import json
import pickle
import os
import sys


def read_json(filepath: str):
    # open specific file
    f = open(filepath)
    # specifies json type and loads into data
    data = json.loads(f.read())
    return data
    # pass  # escape return


def read_all_json_files(dirpath: str):

    for files in dirpath:
        if '.json' in files:
            read_json(files)
    pass


def write_pickle(filename: str, data):
    f = open(filename)
    jdata = json.loads(f.read())
    pdata = pickle.loads(data)
    pass


def is_dir(dirpath):
    return os.path.isdir(dirpath)


def is_json(filename):
    return 'json' in filename


def load_pickle(filepath: str):
    f = open(filepath)
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('incorrect arugments')
        exit()
    filename = sys.argv[1]
    if is_dir(filename):
        read_all_json_files(filename)
    elif is_json(filename):
        read_json(filename)
    else:
        print('incompatible filetype')
        exit()
