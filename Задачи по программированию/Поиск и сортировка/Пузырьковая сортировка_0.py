# Пузырьковая сортировка_0
# Требуется отсортировать массив по неубыванию методом "пузырька".
#
# Входные данные
#
# В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива. Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
#
# Выходные данные
#
# Вывести получившийся массив.
#
# Sample Input:
#
# 5
# 5 4 3 2 1
# Sample Output:
#
# 1 2 3 4 5

n = int(input())
arr = list(map(int, input().split(" ")))

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(*arr)