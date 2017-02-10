# Необходимо разработать функцию для выборки определенного числа тест-кейсов из файла c расширением txt.
# На вход функции подаются 2 параметра: путь к исходному файлу(обязательный параметр),
# который содержит таблицу в текстовом виде (разделителями являются табуляция и символ новой строки)
# и необязательный параметр — количество строк, которые надо выбрать из файла.
# По умолчанию необходимо выбрать 10 строк.

import os

# Enter path
path_to_file = input('Enter the path where .txt file is located: ')
while os.path.exists(path_to_file) is False:
    path_to_file = input('The entered path to file is incorrect. Try again: ')

# Enter a count of strings
try:
    number_of_strings = int(input('Enter a number of strings: '))
except ValueError:
    number_of_strings = input('A number of strings is incorrect. Try again: ')

number_of_strings = number_of_strings or 10

print(number_of_strings)
file = open(path_to_file)

file.close()
