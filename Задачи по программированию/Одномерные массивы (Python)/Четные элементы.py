# Четные элементы
# Выведите все четные элементы списка.
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
# 1 2 2 3 3 3 4
# Sample Output:
#
# 2 2 4

arr = input().split(" ");
othArr = [];

for i in range(len(arr)):
    if int(arr[i]) % 2 == 0:
        othArr.append(arr[i]);
print(" ".join(othArr));