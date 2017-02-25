# Необходимо разработать функцию для выборки определенного числа тест-кейсов из файла c расширением txt.
# На вход функции подаются 2 параметра: путь к исходному файлу(обязательный параметр),
# который содержит таблицу в текстовом виде (разделителями являются табуляция и символ новой строки)
# и необязательный параметр — количество строк, которые надо выбрать из файла.
# По умолчанию необходимо выбрать 10 строк.
#  Алгоритм работы функции:
# 1) Считать содержимое исходного файла;
# 2) Вырезать заданное число строк из файла случайным образом;
# 3) Записать выбранные строки в результирующий файл. Путь к этому файлу и его расширение совпадает
#    с путем и расширением исходного файла, а имя формируется как имя исходного файла + «_res»;
# 4) Сохранить исходный файл без выбранных строк;
# 5) Вернуть необходимо путь к результирующему файлу.

import os
import random
import re

# Enter path
path_to_file = input('Enter the path where .txt file is located: ')
while not os.path.exists(path_to_file):
    path_to_file = input('The entered path to file is incorrect. Try again: ')

# Open the file for count a number of strings
file = open(path_to_file)
lines = file.readlines()
file.close()

# Enter a count of strings
while True:
    try:
        number_of_strings = input('Enter a valid number of strings not more than ' + str(len(lines)-1) + ' : ')
        if not number_of_strings:
            break
        number_of_strings = int(number_of_strings)
        while number_of_strings > len(lines) - 1:
            number_of_strings = input(
                'Enter a valid number of strings not more than ' + str(len(lines)-1) + ' : ')
            number_of_strings = int(number_of_strings)
    except ValueError:
        continue
    break
number_of_strings = number_of_strings or 10


def select_cases(path_to_file, number_of_strings):
    # Open file
    file = open(path_to_file, 'r')

    # Create and open new file with "_res" using re
    (path, filename) = os.path.split(path_to_file)
    new_file_res = re.sub(r".txt", r"_res.txt", filename)
    file_res_path = os.path.join(path, new_file_res)
    file_res = open(file_res_path, 'w+')

    lines = file.readlines()
    file.close()
    strings = len(lines)

    file_res.write(lines[0])
    for n in range(number_of_strings):
        rand = random.randint(1, strings - 1)
        file_res.write(lines[rand] + '\n')
        lines.pop(rand)
        strings = strings - 1

    file = open(path_to_file, 'w')
    for i in lines:
        file.write(i + '\n')
    file.close()
    file_res.close()

    return os.path.abspath(file_res_path)


res = select_cases(path_to_file, number_of_strings)
print("Path for your file with test cases: " + res)
