# Определить количество пассажиров, севших в порту Шербур,
# в возрастном интервале средний возраст +- 5 лет и сколько из них выжило

import csv

file = open("titanic.csv", "r")
rows = list(csv.reader(file))

# Переменные для подсчета
count_survivor = 0
count_all = 0
sum = 0
num = 0
age_list = []  # список возрастов

max_age = -1
min_age = 200

for i in rows:
    if i[1] == "1" or i[1] == "0":
        if i[5] != "" and i[5] != " ":
            if float(i[5]) > max_age:
                max_age = float(i[5])
            elif float(i[5]) < min_age:
                min_age = float(i[5])

median_age = (max_age + min_age) / 2

for i in rows:
    if i[1] == "1" or i[1] == "0":
        if i[5] != "" and i[5] != " ":
            if abs(median_age - float(i[5])) <= 5:
                count_all += 1
for i in rows:
    if i[1] == "1" or i[1] == "0":
        if i[11] == "C":  # Проверка на соответствие условию C = Cherbourg Q = Queenstown S = Southampton
            if i[5] != "" and i[5] != " ":  # Проверка на пустую строку
                count_all += 1
                if i[1] == "1":
                    count_survivor += 1

print(f"Пассажиров, севших в порту Шейбур : {count_all}\nИз них выжило: {count_survivor}")