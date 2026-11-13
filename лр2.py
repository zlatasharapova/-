from csv import reader
from datetime import datetime
import os
import xml.etree.ElementTree as ET

def open_table():
    try:
        with open('books-en.csv', 'r',  encoding='cp1251', newline='') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            table = table[1:]
            return table
    except FileNotFoundError:
        print('Файл не найден!')
        return 0
table = open_table()
def count_long(table):
    flag = 0
    for row in table:
        if len(row[1]) > 30:
            flag += 1
    print('Записей с названием длиннее 30 символов:', flag)
    input('Нажмите Enter')

def find_string(searchline, string):
    string = string.lower()
    index = string.find(searchline.lower())
    return index

def search(table):
    searchline = input('Введите автора (0 - назад): ')
    if searchline in ['0', '']:
        return 0
    output = open('result.txt', 'w', encoding='utf-8')
    output.write(f'Поиск от: {datetime.today()}\n\n')
    flag = 0
    for row in table:
        if find_string(searchline, row[2]) != -1 and row[3].strip() in ['1991', '1996']:
            print(f'{row[2]}. {row[1]} - {row[3]}')
            output.write(f'{row[2]}. {row[1]} - {row[3]}\n')
            flag += 1
    if flag == 0:
        print('Ничего не найдено! (выдаются только книги 1991 и 1996 годов)')
    else:
        print(f'Найдено позиций: {flag}')
    input('Нажмите Enter')
    output.close()
search(table)

def bibliography(table):
    output = open('bibliography.txt', 'w', encoding='utf-8')
    number = 1
    for row in table[:20]:
        output.write(f'{number}. {row[2]}. {row[1]} - {row[3]}\n')
        number += 1
    output.close()
    print('Список из 20 записей сохранён в bibliography.txt')
    input('Нажмите Enter')

def parse_currency():
    try:
        root = ET.parse('currency.xml').getroot()
    except FileNotFoundError:
        print('Файл currency.xml не найден!')
        input('Нажмите Enter')
        return 0
    names = []
    values = []
    for valute in root.iter('Valute'):
        names.append(valute.findtext('Name'))
        values.append(float(valute.findtext('Value').replace(',', '.')))
    print(f'Дата курсов: {root.get("Date")}')
    print(f'Валют в файле: {len(names)}')
    for i in range(len(names)):
        print(f'{names[i]} - {values[i]}')
    input('Нажмите Enter')

def publishers(table):
    unique = set()
    for row in table:
        unique.add(row[4].strip())
    unique = sorted(unique)
    print('Издательств без повторений:',len(unique))
    for name in unique:
        print(name)
    input('Нажмите Enter')


def top_books(table):
    sorted_table = sorted(table, key=lambda row: int(row[5]), reverse=True)
    number = 1
    for row in sorted_table[:20]:
        print(f'{number}. {row[2]}. {row[1]} - {row[3]} (скачиваний: {row[5]})')
        number += 1
    input('Нажмите Enter')

while True:
    os.system('clear')
    table = open_table()
    if table == 0:
        break
    print('Меню:\n1 - Количество названий длиннее 30 символов\n2 - Поиск книги по автору'
          '\n3 - Библиографические ссылки (20 записей)\n4 - Курсы валют\n5 - Издательства без повторений\n6 - 20 самых популярных книг\n0 - Выход')
    menu = input('Выберите пункт меню: ')
    match menu:
        case '1':
            count_long(table)
        case '2':
            search(table)
        case '3':
            bibliography(table)
        case '4':
            parse_currency()
        case '5':
            publishers(table)
        case '6':
            top_books(table)
        case '0':
            break
        case _:
            print('Нет пункта меню, нажмите Enter')
            input()