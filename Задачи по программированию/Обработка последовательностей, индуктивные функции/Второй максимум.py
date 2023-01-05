# Второй максимум
# Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# 1
# 7
# 9
# 0
# Sample Output:
#
# 7

arr = [];
while True:
    a = int(input());
    if a == 0:
        break;
    else:
        arr.append(a);

max = arr[0];
for i in range(1, len(arr)):
    if arr[i] > max: max = arr[i];

n = 0;
for i in range(0, len(arr)):
    if arr[i] == max:
        n += 1;

for i in range(n):
    arr.remove(max);

max = arr[0];
for i in range(1, len(arr)):
    if arr[i] > max: max = arr[i];
print(max);