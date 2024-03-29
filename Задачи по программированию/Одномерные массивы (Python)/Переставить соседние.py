# Переставить соседние
# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.). Если элементов нечетное число, то последний элемент остается на своем месте.
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
# 1 2 3 4 5
# Sample Output:
#
# 2 1 4 3 5

arr = input().split(" ");

if len(arr) % 2 == 0:
    for i in range(1, len(arr), 2):
        arr[i], arr[i-1] = arr[i-1], arr[i];
if len(arr) % 2 == 1:
    for i in range(1, len(arr)-1, 2):
        arr[i], arr[i-1] = arr[i-1], arr[i];
print(" ".join(arr));