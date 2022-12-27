#!/bin/python3

import os
from sys import argv

def doublon():
    file = {}

    try:
        chemin = argv[1]
        output_file_name = argv[2]

        for (repertoire, sousRepertoire, fichiers) in os.walk(chemin):
            print(repertoire)
            for i in fichiers:
                name = os.path.splitext(i)
                try:
                    if file[name[0]]:
                        file[name[0]].append(repertoire)
                except:
                    file[name[0]] = [repertoire]

        back = "\n  "
        if os.path.exists(f"{output_file_name}.txt"):
            os.remove(f"{output_file_name}.txt")
            print(f"{output_file_name}.txt removed")

        for keys, values in file.items():
            if len(values) > 1:
                with open(f"{output_file_name}.txt", "a") as output:
                    output.write(f"""
{keys} :
  {back.join(values)}
                             """)
        print(f"{output_file_name}.txt created")
        print(f"Succesfull operation")

    except IndexError:
        print("""error : argument(s) missing
             "simili-finder <folder path> <output file name>\"""")

def start_doublon():
    file = {}

    try:
        chemin = argv[1]
        output_file_name = argv[2]
        nbr_chr = int(argv[3])

        for (repertoire, sousRepertoire, fichiers) in os.walk(chemin):
            print(repertoire)
            for i in fichiers:
                name = os.path.splitext(i)
                if len(name[0]) > nbr_chr:
                    name = name[0][:nbr_chr]
                else:
                    name = name[0]
                try:
                    if file[name]:
                        file[name].append(repertoire)
                except:
                    file[name] = [repertoire]

        back = "\n  "
        if os.path.exists(f"{output_file_name}.txt"):
            os.remove(f"{output_file_name}.txt")
            print(f"{output_file_name}.txt removed")

        for keys, values in file.items():
            if len(values) > 1:
                with open(f"{output_file_name}.txt", "a") as output:
                    output.write(f"""
{keys} :
  {back.join(values)}
                                 """)
        print(f"{output_file_name}.txt created")
        print(f"Succesfull operation")

    except IndexError:
        print("error : argument(s) missing \n \"simili-finder <folder path> <output file name> <num char>\"")

try:
    arg = argv[3]
    start_doublon()
except:
    doublon()
