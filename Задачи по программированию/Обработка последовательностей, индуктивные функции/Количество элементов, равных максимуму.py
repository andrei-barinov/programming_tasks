# Количество элементов, равных максимуму
# Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел (не считая завершающего числа 0). Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
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
# 3
# 3
# 1
# 0
# Sample Output:
#
# 2

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
print(n);