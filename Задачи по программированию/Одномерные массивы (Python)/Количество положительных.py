# Количество положительных
# Найдите количество положительных элементов в данном списке.
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
# 1 -2 3 -4 5
# Sample Output:
#
# 3

arr = input().split(" ");
tmp = 0;

for i in range(len(arr)):
    if int(arr[i]) > 0:
        tmp += 1;
print(tmp);