# Необходимо разработать функцию для выборки определенного числа тест-кейсов из файла c расширением txt.
# На вход функции подаются 2 параметра: путь к исходному файлу(обязательный параметр),
# который содержит таблицу в текстовом виде (разделителями являются табуляция и символ новой строки)
# и необязательный параметр — количество строк, которые надо выбрать из файла.
# По умолчанию необходимо выбрать 10 строк.

import os
import random
import re

# Enter path
path_to_file = input('Enter the path where .txt file is located: ')
while not os.path.exists(path_to_file):
    path_to_file = input('The entered path to file is incorrect. Try again: ')

# Enter a count of strings
while True:
    try:
        number_of_strings = input('Enter a valid number of strings: ')
        if not number_of_strings:
            break
        number_of_strings = int(number_of_strings)
    except ValueError:
        continue
    break

number_of_strings = number_of_strings or 10

# Open file
file = open(path_to_file)

# Create and open new file with "_res" using re
(path, filename) = os.path.split(path_to_file)
new_file_res = re.sub(r".txt", r"_res.txt", filename)
file_res = os.path.join(path, new_file_res)
file_res = open(file_res, 'w')

lines = file.readlines()
strings = len(lines)

file_res.write(lines[0])
for n in range(number_of_strings):
    file_res.write(lines[random.randint(1, strings-1)] + '\n')

file.close()
file_res.close()

print("Done. Check the created file near the parent file is located. ")
