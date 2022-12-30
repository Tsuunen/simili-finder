#!/bin/python3

import os
import time


def help():
    print("""
Simili-finder v0.5.1

commands :
    scan : find file with some similarity
        -o : set the output file name (default = "simili-finder_scan_[timezone].txt")
        -d : set the folder to scan (default = current folder)
        -a : set additional parameter :
                "word" to shearch file with the same word in it
                <number (int)> to shearch file who have the same x first character

    find : find specific file
        -o : set the output file name (default = "simili-finder_find_[timezone].txt")
        -d : set the folder to look for the file (default = current folder)
        -f : name of the file (mandatory)

    help : see the command list

    quit : quit to program
            
        """)


def get_parameter(parameter: list) -> dict:
    options = {f"{parameter[0]}": "oui"}

    for opt in range(len(parameter)):
        if parameter[0] == "scan":
            if parameter[opt] == "-o":
                options['output_file_name'] = parameter[opt + 1]
            elif parameter[opt] == "-d":
                options["directory"] = parameter[opt + 1]
            elif parameter[opt] == "-a":
                options["add_par"] = parameter[opt + 1]

        elif parameter[0] == "find":
            if parameter[opt] == "-o":
                options["output_file_name"] = parameter[opt + 1]
            elif parameter[opt] == "-d":
                options["directory"] = parameter[opt + 1]
            elif parameter[opt] == "-f":
                options["file"] = parameter[opt + 1]

        else:
            print("Simili-finder: invalid syntax")
            return options
    return options


def doublon(path):
    result = {}
    delimiter = os.pathsep

    for (directory, o, files) in os.walk(path):
        print(directory)
        for i in files:
            name = os.path.splitext(i)
        try:
            if result[name[0]]:
                result[name[0]].append(directory + delimiter + i)
        except:
            result[name[0]] = [directory + delimiter + i]
    return result


def start_doublon(path: str, nbr_char: int):
    result = {}
    delimiter = os.path.sep

    for (directory, o, files) in os.walk(path):
        print(directory)
        for i in files:
            name = os.path.splitext(i)
            if len(name[0]) > nbr_char:
                name = name[0][:nbr_char]
            else:
                name = name[0]
            try:
                if result[name]:
                    result[name].append(directory + delimiter + i)
            except:
                result[name] = [directory + delimiter + i]
    return result


def word_doublon(path):
    result = {}
    delimiter = os.pathsep

    for (directory, o, files) in os.walk(path):
        print(directory)
        for i in files:
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
                    if result[j]:
                        result[j].append(directory + delimiter + i)
                except:
                    result[j] = [directory + delimiter + i]
    return result


def find(path, file_name):
    result = {}
    delimiter = os.pathsep

    for (directory, o, files) in os.walk(path):
        print(directory)
        for i in files:
            name = os.path.splitext(i)
            if name[0] == file_name:
                try:
                    if result[name[0]]:
                        result[name[0]].append(directory + delimiter + i)
                except:
                    result[name[0]] = [directory + delimiter + i]

    return result


help()

while True:
    command = input(" > ")
    parameter = command.split(" ")

    if parameter[0] == "help":
        help()
    elif parameter[0] == "quit":
        break
    else:
        options = get_parameter(parameter)

        if parameter[0] == "scan":
            try:
                output_file_name = options["output_file_name"]
            except:
                t = time.localtime()
                output_file_name = f"simili-finder_scan_{t[3]}:{t[4]}:{t[5]}"
            try:
                if not os.path.exists(options["directory"]):
                    print("simili-finder: directory not found")
                    continue
                directory = options["directory"]
            except:     
                directory = "."
            try:
                add_option = options["add_par"]
            except:
                add_option = False

            print(add_option)
            if not add_option:
                result = doublon(directory)
            else:
                try:
                    add_option = int(add_option)
                    result = start_doublon(directory, add_option)
                except:
                    result = word_doublon(directory)
        
        elif parameter[0] == "find":
            try:
                output_file_name = options["output_file_name"]
            except:
                t = time.localtime()
                output_file_name = f"simili-finder_find_{t[3]}:{t[4]}:{t[5]}"
            try:
                directory = options["directory"]
            except:
                directory = "."
            try:
                file = options["file"]
            except:
                print("Simili-finder: file name mandatory")
                continue
            result = find(directory, file)
        
    if len(result) != 0:
        back = "\n  "
        if os.path.exists(f"{output_file_name}.txt"):
            os.remove(f"{output_file_name}.txt")
            print(f"{output_file_name}.txt")

        for keys, values in result.items():
            if parameter[0] != "find":
                if len(values) > 1:
                    with open(f"{output_file_name}.txt", "a") as out:
                        out.write(f"""
{keys} :
  {back.join(values)}
                                  """)
            else:
                with open(f"{output_file_name}.txt", "a") as out:
                    out.write(f"""
{keys} : 
  {back.join(values)}
                              """)
        print(f"{output_file_name}.txt created")
        print("Succesfull operation")

