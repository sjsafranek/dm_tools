import csv
import json
import requests

url = "https://roll20.net/compendium/compendium/getList?pageName=Monsters%20List&bookName=dnd5e"


'''
// https://roll20.net/compendium/dnd5e/Monsters%20List#content
for (var i=0; i<data.length; i++) {
    if ("—" != data[i]['c'][22]) {
        console.log(data[i]['n'], data[i]['c'])
    }
}
'''


resp = requests.get(url)

monsters = []
data = json.loads(resp.json()['results'])
for row in data:
    # hp
    hp = row['c'][3]
    hp_parts = row['c'][3].split(" (")
    hp_average = hp_parts[0]
    hp_source = hp_average
    if 1 != len(hp_parts):
        hp_source = hp_parts[1].replace(")", "")
    # ac
    ac = row['c'][4]
    ac_parts = ac.split(" (")
    armor_class = ac_parts[0]
    armor_type = ''
    if 1 != len(ac_parts):
        armor_type = ac_parts[1].replace(")", "")
    # saves
    saves = row['c'][20].split(", ")
    str_save = None
    dex_save = None
    con_save = None
    int_save = None
    wis_save = None
    cha_save = None
    for save in saves:
        if "Str" in save:
            str_save = save.replace("Str ", "")
        if "Dex" in save:
            dex_save = save.replace("Dex ", "")
        if "Con" in save:
            con_save = save.replace("Con ", "")
        if "Int" in save:
            int_save = save.replace("Int ", "")
        if "Wis" in save:
            wis_save = save.replace("Wis ", "")
        if "Cha" in save:
            cha_save = save.replace("Cha ", "")
    # monster info
    monster = {
        'name': row['n'],
        'size': row['c'][0],
        'type': row['c'][1],
        'alignment': row['c'][2],
        'hp_average': hp_average,
        'hp_source': hp_source,
        # 'ac': row['c'][4],
        'armor_class': armor_class,
        'armor_type': armor_type,
        'speed': row['c'][5],
        'cr': row['c'][6],
        'xp': row['c'][7].replace(",", ""),
        'str': row['c'][8],
        'str_mod': row['c'][9],
        'dex': row['c'][10],
        'dex_mod': row['c'][11],
        'con': row['c'][12],
        'con_mod': row['c'][13],
        'int': row['c'][14],
        'int_mod': row['c'][15],
        'wis': row['c'][16],
        'wis_mod': row['c'][17],
        'cha': row['c'][18],
        'cha_mod': row['c'][19],
        # 'saves': row['c'][20],
        'str_save': str_save,
        'dex_save': dex_save,
        'con_save': con_save,
        'int_save': int_save,
        'wis_save': wis_save,
        'cha_save': cha_save,
        #.end
        'skills': row['c'][21],
        'vulnerabilities': row['c'][22],
        # 'unknown2': row['c'][23],
        'damage_resistances': row['c'][24],
        'damage_immunities': row['c'][25],
        'condition_immunities': row['c'][26],
        'passive_perception': row['c'][27],
        'senses': row['c'][28],
        'launguages': row['c'][29],
        'special_abilties': row['c'][30],
        'actions': row['c'][31],
        # 32, 33, 34, 35
        'reactions': row['c'][37],
        'legnedary_actions': row['c'][38]
    }
    for key in monster:
        if "—" == monster[key]:
            monster[key] = None
        elif monster[key]:
            monster[key] = monster[key].replace("\\u2022", "")
            monster[key] = monster[key].replace(",", ";")
    monsters.append(monster)

with open('monsters/roll20_compendium_monsters.tsv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(monsters[0].keys()), delimiter="\t")
    writer.writeheader()
    writer.writerows(monsters)




import pandas as pd

file1 = 'monsters/monsters_base.tsv'
df1 = pd.read_csv(file1, sep='\t')
df1['Environment'] = df1['Environment'].str.replace(',',';')

file2 = 'monsters/roll20_compendium_monsters.tsv'
df2 = pd.read_csv(file2, sep='\t')

del df1['NPC Name']
del df1['Size']
del df1['Type']
del df1['Alignment']
del df1['Challenge']
del df1['XP']
del df1['Description']

df3 = pd.merge(df1[df1.Source == "MM"], df2, how='left', left_on="Name", right_on="name")

del df3['name']
df3.to_csv("MONSTERS.csv", index=False)

# import sqlite3
# conn = sqlite3.connect("monsters.db")
# df3.to_sql("monsters", conn, if_exists="replace")
