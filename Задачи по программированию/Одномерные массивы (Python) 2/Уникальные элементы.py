# Уникальные элементы
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
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
# 1 2 2 3 3 3
# Sample Output:
#
# 1

arr = input().split(" ")
arrTmp = [];
tmp = 0;

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        if arr[i] == arr[j]:
            tmp +=1
    if tmp == 0:
        arrTmp.append(arr[i])
    tmp = 0
print(*arrTmp);