# Самое частое число
# Дан список. Не изменяя его и не используя дополнительные списки, определите, какое число в этом списке встречается чаще всего.
#
# Если таких чисел несколько, выведите любое из них.
#
# Входные данные
#
# Вводится список чисел. Все числа списка находятся на одной строке.
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# 1 2 3 2 3 3
# Sample Output:
#
# 3

arr = input().split(" ")

index = 0
indexSave = 0
tmp = 0
tmpSave = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        if arr[i] == arr[j]:
            tmp += 1
            index = j
    if tmp > tmpSave:
        tmpSave = tmp
        indexSave = index
    tmp = 0
print(arr[indexSave]);