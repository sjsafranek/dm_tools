import os
from .utils import csv2dict
from .utils import filterDictList

data_dir = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    "data"
)

files = {
    'MONSTERS': os.path.join(data_dir, 'MONSTERS.csv')
}

tables = {
    "MONSTERS": csv2dict(files['MONSTERS'])
}

def getMonstersByCR(cr):
    cr = str(cr)
    return filterDictList(tables['MONSTERS'], 'cr', cr)

def getMonsterByName(name):
    return filterDictList(tables['MONSTERS'], 'Name', name)
