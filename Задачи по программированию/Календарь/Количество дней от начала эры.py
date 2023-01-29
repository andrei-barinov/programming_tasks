# Количество дней от начала эры
# Требуется посчитать количество дней от начала эры до данного дня включительно. Началом эры считается первое января первого года.
#
# Входные данные
#
# В единственной строке входного файла находится дата в формате ДДММГГГГ.
#
# Выходные данные
#
# Выведите искомое количество дней.
#
# Sample Input:
#
# 02010001
# Sample Output:
#
# 2

date = str(input())
day = int(date[:2])
month = int(date[2:4])
year = int(date[4:])

total = 0

for i in range(1, year):
    if i % 4 == 0 and i % 100 != 0:
        total += 366
    elif i % 400 == 0:
        total += 366
    else:
        total += 365

Calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if year % 4 == 0 and year % 100 != 0:
    Calendar[2] = 29
elif year % 400 == 0:
    Calendar[2] = 29

for i in range(1, month):
    total += Calendar[i]

total += day

print(total)