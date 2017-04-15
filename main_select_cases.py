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
import re
from select_cases_method import select_cases

# Enter path
path_to_file = input('Enter the path where .txt file is located: ')
while not os.path.exists(path_to_file):
    path_to_file = input('The entered path to file is incorrect. Try again: ')

# Create and open new file with "_res" using re
(path, filename) = os.path.split(path_to_file)
new_file_res = re.sub(r".txt", r"_res.txt", filename)
file_res_path = os.path.join(path, new_file_res)

# Open the file for count a number of strings
file = open(path_to_file)
lines = file.readlines()
file.close()

# Enter a count of strings
counter = 0
max_counter = 5
while True:
    try:
        if counter == max_counter:
            print('You spent your attempts for entering the correct value. The program will closed.')
            exit(0)
        number_of_strings = input('Enter a valid number of strings not more than ' + str(len(lines) - 1) + ' : ')
        counter += 1
        if not number_of_strings:
            break
        number_of_strings = int(number_of_strings)
        if number_of_strings < len(lines):
            break
        else:
            continue
    except ValueError:
        continue
number_of_strings = number_of_strings or 10

res = select_cases(path_to_file, number_of_strings, file_res_path)
print("Path for your file with test cases: " + res)
