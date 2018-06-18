import os
import json
import math
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
        self._data = monster
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
        self.ac = int(float(monster['armor_class']))
        self.alignment = monster['alignment']
        self.size = monster['size']
        self.cr = monster['cr']
        self.speed = monster['speed']
        self.page = monster['Page']
        self.hp = self.getHP()
        self.special_abilties = Actions(self._data['special_abilties'])
        self.reactions = Actions(self._data['reactions'])
        self.actions = Actions(self._data['actions'])
        self.legnedary_actions = Actions(self._data['legnedary_actions'])

    def getHP(self):
        source = self._data['hp_source']
        parts = source.split('d')
        n = int(parts[0])
        d = parts[1]
        m = 0
        if '-' in d:
            arr = d.split('-')
            d = arr[0]
            m = arr[1]
        if '+' in d:
            arr = d.split('+')
            d = arr[0]
            m = arr[1]
        d = int(d)
        m = int(m)
        return dice.rollDice(n, d) + m

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

    def dealDamage(self, dmgType, amount):
        if dmgType.lower() in self._data['damage_resistances'].lower():
            amount = math.ceil(amount/2)
        elif dmgType.lower() in self._data['damage_immunities'].lower():
            amount = 0
        self.hp -= amount

    def rollInitiative(self):
        return dice.d20() + self.getAbilityMod('DEX')


class Actions(object):

    def __init__(self, actions):
        self.actions = {}
        self._data = []
        actions = actions.replace(';',',')
        if actions and '' != actions:
            self._data = json.loads(actions)
            for action in self._data:
                self.actions[action['Name']] = action

    def getActions(self):
        return list(self.actions.keys())



"""

import dm_tools

monsters = dm_tools.monsters.getMonsterByName("Goblin")
goblin = dm_tools.monsters.Monster(monsters[0])
goblin.rollInitiative()

monsters = dm_tools.monsters.getMonsterByName("Ancient Red Dragon")
dragon = dm_tools.monsters.Monster(monsters[0])





'special_abilties': '[{"Name":"Nimble Escape";"Desc":"The goblin can take the Disengage or Hide action as a bonus action on each of its turns."}]'
'reactions': ''
'actions': '[{"Name":"Scimitar";"Type Attack":"Weapon Attack";"Type":"Melee";"Hit Bonus":"4";"Reach":"5 ft.";"Target":"one target";"Damage":"1d6 + 2";"Damage Type":"slashing"};{"Name":"Shortbow";"Type Attack":"Weapon Attack";"Type":"Ranged";"Hit Bonus":"4";"Reach":"80/320 ft.";"Target":"one target";"Damage":"1d6 + 2";"Damage Type":"piercing"}]'
legnedary_actions


   'Source': 'MM'
   'launguages': 'Common; Goblin'
   'SRD': 'Y'
   'condition_immunities': ''

   'Environment': 'Forest; Grassland; Hills; Underdark'
   'Reference': 'MM166'
   'armor_type': 'Leather Armor; Shield'
   'vulnerabilities': ''
   'passive_perception': '9.0'



   'Tags/Lair': 'goblinoid'
   'senses': 'Darkvision 60 Ft.'
   'skills': 'Stealth +6'

"""
