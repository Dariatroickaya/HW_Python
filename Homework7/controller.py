from os.path import exists
from read import reading
from create import creating


def file_none():
    path = 'Phone_dictionary.csv'
    valid = exists(path)
    if not valid:
        print(creating())
    reading()