#!/bin/python3

import os
from sys import argv

def doublon(chemin):
    file = {}

    for (repertoire, sousRepertoire, fichiers) in os.walk(chemin):
        print(repertoire)
        for i in fichiers:
            name = os.path.splitext(i)
            try:
                if file[name[0]]:
                    file[name[0]].append(repertoire + "/" + i)
            except:
                file[name[0]] = [repertoire + "/" + i]
    return file


def start_doublon(chemin, nbr_char):
    file = {}

    for (repertoire, sousRepertoire, fichiers) in os.walk(chemin):
        print(repertoire)
        for i in fichiers:
            name = os.path.splitext(i)
            if len(name[0]) > nbr_char:
                name = name[0][:nbr_char]
            else:
                name = name[0]
            try:
                if file[name]:
                    file[name].append(repertoire + "/" + i)
            except:
                file[name] = [repertoire + "/" + i]
    return file


def word_doublon(chemin):
    file = {}

    for (repertoire, sousRepertoire, fichiers) in os.walk(chemin):
        print(repertoire)
        for i in fichiers:
            der_indice = -1
            mots = []
            for k in range(len(i)):
                if i[k] in [" ", "/", "-", "_", ",", ".", "'", "(", ")"]:
                    mots.append(i[der_indice + 1:k])
                    der_indice = k
            if len(mots) == 0:
                mots.append(i)
            for j in mots:
                try:
                    if file[j]:
                        file[j].append(repertoire + "/" + i)
                except:
                    file[j] = [repertoire + "/" + i]
    return file


try:
    chemin = argv[1]
    output_file_name = argv[2]

    try:
        arg = argv[3]
        try:
            arg = int(arg)
            file = start_doublon(chemin, arg)
        except:
                file = word_doublon(chemin)
    except:
        file = doublon(chemin)

    back = "\n  "
    if os.path.exists(f"{output_file_name}.txt"):
        os.remove(f"{output_file_name}.txt")
        print(f"{output_file_name}.txt removed")

    for keys, values in file.items():
        if len(values) > 1:
            with open(f"{output_file_name}.txt", "a") as out:
                out.write(f"""
{keys}:
  {back.join(values)}
                      """)
    print(f"{output_file_name}.txt created")
    print("Succesfull operation")

except:
    print("error : see more info on github.com/Tsuunen/simili-finder")
        
