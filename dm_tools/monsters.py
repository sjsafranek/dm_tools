import os
from dm_tools.utils import csv2dict
from dm_tools.utils import filterDictList
import dm_tools.dice as dice

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


class Monster(object):
    def __init__(self, monster):
        self.name = monster['Name']
        self.type = monster['type']
        self.xp = float(monster['xp'])
        self.abilities = {
            'STR': int(float(monster['str'])),
            'DEX': int(float(monster['dex'])),
            'CON': int(float(monster['con'])),
            'INT': int(float(monster['int'])),
            'WIS': int(float(monster['wis'])),
            'CHA': int(float(monster['cha']))
        }
        self.ac = monster['armor_class'] #'15.0'
        self._data = monster

    def getAbilityMod(self, ability):
        score = self.abilities[ability.upper()]
        return int((score - 10)/2)

    def getSave(self, ability):
        key = '{0}_save'.format(ability.lower())
        if '' != self._data[key]:
            return int(self._data[key])
        else:
            return self.getAbilityMod(ability)

    def rollSave(self, ability, advantage=False):
        if advantage:
            return max([ dice.d20(), dice.d20() ]) + self.getSave(ability)
        return dice.d20() + self.getSave(ability)

"""

import dm_tools

monsters = dm_tools.monsters.getMonsterByName("Goblin")
goblin = dm_tools.monsters.Monster(monsters[0])


 'special_abilties'
  'special_abilties': '[{"Name":"Nimble Escape";"Desc":"The goblin can take the Disengage or Hide action as a bonus action on each of its turns."}]'
   'Source': 'MM'
   'launguages': 'Common; Goblin'
   'hp_average': '7.0'
   'SRD': 'Y'
   'hp_source': '2d6'
   'condition_immunities': ''
   'reactions': ''
   'speed': '30 ft.'
   'Page': '166.0'
   'actions': '[{"Name":"Scimitar";"Type Attack":"Weapon Attack";"Type":"Melee";"Hit Bonus":"4";"Reach":"5 ft.";"Target":"one target";"Damage":"1d6 + 2";"Damage Type":"slashing"};{"Name":"Shortbow";"Type Attack":"Weapon Attack";"Type":"Ranged";"Hit Bonus":"4";"Reach":"80/320 ft.";"Target":"one target";"Damage":"1d6 + 2";"Damage Type":"piercing"}]'
   'Environment': 'Forest; Grassland; Hills; Underdark'
   'Reference': 'MM166'
   'armor_type': 'Leather Armor; Shield'
   'vulnerabilities': ''
   'passive_perception': '9.0'
   'legnedary_actions': ''
   'damage_resistances': ''
   'alignment': 'Neutral Evil'
   'size': 'Small'

   'cr': '1/4'
   'damage_immunities': ''

   'Tags/Lair': 'goblinoid'
   'senses': 'Darkvision 60 Ft.'
   'skills': 'Stealth +6'

"""
