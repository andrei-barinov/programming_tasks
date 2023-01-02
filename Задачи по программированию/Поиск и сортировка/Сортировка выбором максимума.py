# Сортировка выбором максимума
# Требуется отсортировать массив по неубыванию методом "выбор максимума".
#
# Входные данные
#
# В первой строке вводится одно натуральное число N, не превосходящее 1000 – размер массива. Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
#
# Выходные данные
#
# Вывести получившийся массив.
#
# Sample Input:
#
# 2
# 3 1
# Sample Output:
#
# 1 3

n = int(input())
arr = list(map(int, input().split(" ")))

for i in range(n):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            arr[j], arr[i] = arr[i], arr[j]
print(*arr)