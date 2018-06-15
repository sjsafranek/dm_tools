import csv

def csv2dict(file):
    data = []
    with open(file, newline='') as fileHandler:
        reader = csv.DictReader(fileHandler)
        for row in reader:
            data.append(row)
    return data

# def tsv2dict(file):
#     data = []
#     with open(file, newline='') as fileHandler:
#         reader = csv.DictReader(fileHandler, delimeter='\t')
#         for row in reader:
#             data.append(row)
#     return data

def filterDictList(table, attr, value):
    return [elem for elem in table if elem[attr] == value]
