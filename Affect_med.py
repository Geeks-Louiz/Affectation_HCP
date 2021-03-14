# -*- coding: utf-8 -*-

import pandas as pd
Dict_stoke_med={}
Dict_stoke_del={}
Dict_longueur_del={}
Dict_longueur_med={}
temp={}
Affected={}

Dict_stoke_med.clear()
Dict_stoke_del.clear()
Dict_longueur_del.clear()
Dict_longueur_med.clear()
Affected.clear()
temp.clear()


with open("/content/Work_HCP_next.csv", 'r') as file:
    for line in file.readlines():
        (key1, value) = line.split(';')

        if key1 not in Dict_stoke_del:
            Dict_stoke_del[key1] = [value]

        else:
            Dict_stoke_del[key1].append(value)
Dict_stoke_del.pop('delegue', None)

print(Dict_stoke_del)

for key in Dict_stoke_del:
    longueur=len(Dict_stoke_del[key])
    Dict_longueur_del[key]=longueur

with open("../Work_HCP_next.csv", 'r') as file:
   for line in file.readlines():
        (value, key) = line.split(';')

        if key not in Dict_stoke_med:
            Dict_stoke_med[key] = [value]

        else:
            Dict_stoke_med[key].append(value)
Dict_stoke_med.pop('med\n', None)
print(Dict_stoke_med)

for key in Dict_stoke_med:
    longueur=len(Dict_stoke_med[key])
    Dict_longueur_med[key]=longueur    

print(Dict_longueur_del)
print(Dict_longueur_med)

for key in Dict_stoke_med:
   if len(Dict_stoke_med[key])==1:
      Affected[key]=Dict_stoke_med[key]
   else:
    for value in Dict_stoke_med[key]:
      temp[value]=Dict_longueur_del[value]
      key_min=min(temp, key=lambda k: temp[k])
      Affected[key]=key_min
      temp.clear()
print(Affected)
import csv
with open('../result.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in Affected.items():
       writer.writerow([key, value])