# Суперсдвиг
# Дана последовательность из N (1 ≤ N ≤ 100000) целых чисел и число K (|K| ≤ 100000). Сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.
#
# В данной задаче нельзя использовать дополнительные массивы (списки). Обратите внимание, что нужно именно преобразовать имеющийся список и распечатать его целиком, а не создать новый, даже назвав его тем же самым именем (это возможно в языке Python).
#
# Входные данные
#
# В первой строке дано натуральное число N, во второй строке N целых чисел, а в последней целое число K. Все числа во входных данных не превышают 109.
#
# Выходные данные
#
# Требуется вывести полученную последовательность. Числа следует выводить через пробел.
#
# Sample Input:
#
# 5
# 5 3 7 4 6
# 3
# Sample Output:
#
# 7 4 6 5 3

n = int(input());
arr = input().split(" ");
k = int(input());

if k > 0:
    for j in range(k):
        for i in range(len(arr) - 2, -1, -1):
            arr[i], arr[i + 1] = arr[i + 1], arr[i];
else:
    for j in range(-k):
        for i in range(1, len(arr)):
            arr[i], arr[i - 1] = arr[i - 1], arr[i];

print(" ".join(arr));
