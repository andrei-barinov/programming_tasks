# Количество различных элементов - 2
# Дан список. Посчитайте, сколько в нем различных элементов, не изменяя самого списка.
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
# 3 2 1 2 3
# Sample Output:
#
# 3

arr = input().split(" ")
arrTmp = [];
tmp = 0;

for i in range(len(arr)):
    for j in range(len(arrTmp)):
        if arr[i] == arrTmp[j]:
            tmp += 1
    if tmp == 0:
        arrTmp.append(arr[i])
    tmp = 0
print(len(arrTmp));