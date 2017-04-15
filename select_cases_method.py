import random
import os

def select_cases(path_to_file, number_of_strings, file_res_path):
    # Open file
    file = open(path_to_file, 'r')
    file_res = open(file_res_path, 'w')
    # Strings from file -> to list
    lines = file.readlines()
    file.close()
    strings = len(lines)
    # Select string by random, push it to new file and remove from list
    file_res.write(lines[0])
    for n in range(number_of_strings):
        rand = random.randint(1, strings - 1)
        file_res.write(lines[rand])
        lines.pop(rand)
        strings -= 1
    file = open(path_to_file, 'w')
    for i in lines:
        file.write(i)
    file.close()
    file_res.close()
    return os.path.abspath(file_res_path)
