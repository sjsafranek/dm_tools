#
# DMG 136
#

import os
import csv
import random
import numpy as np

from .dice import dice
from .utils import csv2dict
from .utils import filterDictList

data_dir = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    "data"
)

files = {
    "ART_AND_GEMSTONES": os.path.join(data_dir, 'ART_AND_GEMSTONES.csv'),
    "MAGIC_ITEMS": os.path.join(data_dir, 'MAGIC_ITEMS.csv'),
    "INDIVIDUAL_TREASURE": os.path.join(data_dir, 'INDIVIDUAL_TREASURE.csv'),
    "HOARD_TREASURE": os.path.join(data_dir, 'HOARD_TREASURE.csv')
}

tables = {
    'ART_AND_GEMSTONES': csv2dict(files['ART_AND_GEMSTONES']),
    'MAGIC_ITEMS': csv2dict(files['MAGIC_ITEMS']),
    'INDIVIDUAL_TREASURE': csv2dict(files['INDIVIDUAL_TREASURE']),
    'HOARD_TREASURE': csv2dict(files['HOARD_TREASURE'])
}

def newTreasure():
    return {
        'cp': 0,
        'sp': 0,
        'ep': 0,
        'gp': 0,
        'pp': 0,
        'gemstones': [],
        'art_objects': [],
        'magic_items': []
    }


def makeTreasure(opts):
    treasure = newTreasure()
    treasure['cp'] = dice.rollDice( int(opts['CP_n']), int(opts['CP_d']) ) * int(opts['CP_m'])
    treasure['sp'] = dice.rollDice( int(opts['SP_n']), int(opts['SP_d']) ) * int(opts['SP_m'])
    treasure['ep'] = dice.rollDice( int(opts['EP_n']), int(opts['EP_d']) ) * int(opts['EP_m'])
    treasure['gp'] = dice.rollDice( int(opts['GP_n']), int(opts['GP_d']) ) * int(opts['GP_m'])
    treasure['pp'] = dice.rollDice( int(opts['PP_n']), int(opts['PP_d']) ) * int(opts['PP_m'])
    if 'GEMSTONES_n' in opts:
        if 0 != int(opts['GEMSTONES_n']):
            treasure['gemstones'] = [getGemstone(opts['GEMSTONES_c']) for _ in range( dice.rollDice(int(opts['GEMSTONES_n']), int(opts['GEMSTONES_d'])) ) ]
    if 'ARTOBJECTS_n' in opts:
        if 0 != int(opts['ARTOBJECTS_n']):
            treasure['art_objects'] = [getArtObject(opts['ARTOBJECTS_c']) for _ in range( dice.rollDice(int(opts['ARTOBJECTS_n']), int(opts['ARTOBJECTS_d'])) ) ]
    if 'MAGIC_ITEMS_n' in opts:
        magic_items = []
        parts_n = opts['MAGIC_ITEMS_n'].split(';')
        parts_d = opts['MAGIC_ITEMS_d'].split(';')
        parts_t = opts['MAGIC_ITEMS_t'].split(';')
        for i in range(len(parts_n)):
            if 0 != int(parts_n[i]):
                magic_items += [getMagicItem(parts_t[i]) for _ in range(dice.rollDice(int(parts_n[i]), int(parts_d[i])))]
        treasure['magic_items'] = magic_items
    return treasure


# ART_AND_GEMSTONES
def _getArtOrGemstone(_cost, _type):
    # normalize gp
    _cost = str(_cost)
    if "gp" not in _cost:
        _cost = '{0}gp'.format(_cost)
    #.end
    table = [elem for elem in tables['ART_AND_GEMSTONES'] if elem['TYPE'] == _type and elem['COST'] == _cost]
    if 0 == len(table):
        return None
    return "{0} ({1})".format(random.choice(table)['NAME'], _cost)

def getGemstone(gp):
    return _getArtOrGemstone(gp, 'gemstone')

def getArtObject(gp):
    return _getArtOrGemstone(gp, 'art_object')


# MAGIC_ITEMS
def getMagicItem(table_name):
    table = filterDictList(tables['MAGIC_ITEMS'], 'TABLE', table_name)
    items = []
    propabilities = []
    for elem in table:
        items.append(elem['MAGIC_ITEM'])
        parts = elem['PROBABILITY'].split('-')
        if 1 == len(parts):
            propabilities.append(0.01)
        else:
            max_value = int(parts[1])
            min_value = int(parts[0])-1
            if "00" == parts[0]:
                min_value = 100
            if "00" == parts[1]:
                max_value = 100
            probability = ( max_value-min_value ) / 100
            propabilities.append( probability )
    return np.random.choice(
        items,
        1,
        p=propabilities
    )[0]


# INDIVIDUAL_TREASURE
def individual(cr):

    CR = None
    if 0 <= cr and 4 >= cr:
        CR = '0-4'
    elif 5 <= cr and 10 >= cr:
        CR = '5-10'
    elif 11 <= cr and 16 >= cr:
        CR = '11-16'
    elif 17 <= cr:
        CR = '17-20'
    table = filterDictList(tables['INDIVIDUAL_TREASURE'], 'CR', CR)

    rows = []
    propabilities = []
    for elem in table:
        rows.append(elem)
        parts = elem['PROBABILITY'].split('-')
        if 1 == len(parts):
            propabilities.append(0.01)
        else:
            max_value = int(parts[1])
            min_value = int(parts[0])-1
            if "00" == parts[0]:
                min_value = 100
            if "00" == parts[1]:
                max_value = 100
            probability = ( max_value-min_value ) / 100
            propabilities.append( probability )
    row = np.random.choice(
        rows,
        1,
        p=propabilities
    )[0]
    return makeTreasure(row)


# HOARD_TREASURE
def hoard(cr):

    CR = None
    if 0 <= cr and 4 >= cr:
        CR = '0-4'
    elif 5 <= cr and 10 >= cr:
        CR = '5-10'
    elif 11 <= cr and 16 >= cr:
        CR = '11-16'
    elif 17 <= cr:
        CR = '17-20'
    table = filterDictList(tables['HOARD_TREASURE'], 'CR', CR)

    rows = []
    propabilities = []
    for elem in table:
        rows.append(elem)
        parts = elem['PROBABILITY'].split('-')
        if 1 == len(parts):
            propabilities.append(0.01)
        else:
            max_value = int(parts[1])
            min_value = int(parts[0])-1
            if "00" == parts[0]:
                min_value = 100
            if "00" == parts[1]:
                max_value = 100
            probability = ( max_value-min_value ) / 100
            propabilities.append( probability )
    row =  np.random.choice(
        rows,
        1,
        p=propabilities
    )[0]
    return makeTreasure(row)
