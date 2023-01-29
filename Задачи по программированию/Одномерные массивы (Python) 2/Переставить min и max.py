# Переставить min и max
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
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
# 3 4 5 2 1
# Sample Output:
#
# 3 4 1 2 5

inArr = input().split(" ");

arr = [];

for i in range(len(inArr)):
    arr.append(int(inArr[i]));

minEl = min(arr);
maxEl = max(arr);

othArr = [];

for i in range(len(arr)):
    if arr[i] == minEl:
        othArr.append(maxEl);
        continue;
    if arr[i] == maxEl:
        othArr.append(minEl);
        continue;
    othArr.append(arr[i]);
print(" ".join(map(str, othArr)));