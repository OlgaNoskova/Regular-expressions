import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
for person in contacts_list:
    fio_list = []
    fio = " ".join(person[:3])
    fio_list = fio.split()
    for i in range(len(fio_list)):
        person[i] = fio_list[i]
for i in range(len(contacts_list)):
    for j in range(len(contacts_list)):
        if contacts_list[i][0] == contacts_list[j][0] and contacts_list[i][1] == contacts_list[j][1] \
                and contacts_list[i] is not contacts_list[j]:
            if contacts_list[i][2] == '':
                contacts_list[i][2] = contacts_list[j][2]
            if contacts_list[i][3] == '':
                contacts_list[i][3] = contacts_list[j][3]
            if contacts_list[i][4] == '':
                contacts_list[i][4] = contacts_list[j][4]
            if contacts_list[i][5] == '':
                contacts_list[i][5] = contacts_list[j][5]
            if contacts_list[i][6] == '':
                contacts_list[i][6] = contacts_list[j][6]


contacts_resault = []
for contact in contacts_list:
    if contact not in contacts_resault:
        contacts_resault.append(contact)

# pprint(contacts_resault)
for person in contacts_resault:
    for i in range(1, len(contacts_resault)):
        if 'доб.' in person[5]:
            pattern = r'(\+7|8)\s*\(*(\d+)\)*\s*(\d+)-*(\d+)-*(\d+)\s*\(*[доб.]*\s*(\d+)\)*'
            result = re.sub(pattern, r"+7(\2)\3-\4-\5 доб.\6", person[5])
            person[5] = result
        elif '(' in person[5]:
            pattern = r"(\+7|8)\s*\(*(\d+)\)*\s*(\d+)-*(\d+)-*(\d+)\s*"
            result = re.sub(pattern, r"+7(\2)\3-\4-\5", person[5])
            person[5] = result
        else:
            pattern = r"(\+7|8)\s*(\d\d\d)-*(\d)(\d)(\d)-*(\d)(\d)(\d)(\d)"
            result = re.sub(pattern, r"+7(\2)\3\4\5-\6\7-\8\9", person[5])
            person[5] = result


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_resault)