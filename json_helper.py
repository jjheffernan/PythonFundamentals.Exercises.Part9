import json
import pickle


def read_json(filepath: str):
    # open specific file
    f = open(filepath)
    # specifies json type and loads into data
    data = json.loads(f.read())
    pass


def read_all_json_files(dirpath: str):

    for files in dirpath:
        files += 1
    pass


def write_pickle(filename: str, data):
    f = open(filename)
    jdata = json.loads(f.read())
    pdata = pickle.loads(data)
    pass


def load_pickle(filepath: str):
    f = open(filepath)
    pass

