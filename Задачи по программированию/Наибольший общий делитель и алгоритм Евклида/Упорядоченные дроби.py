# Упорядоченные дроби
# Вывести в порядке возрастания все несократимые дроби, заключённые между 0 и 1, знаменатели которых не превышают N.
#
# Входные данные
#
# В первой строке находится единственное число N. 2 <= N <= 255.
#
# Выходные данные
#
# В каждой строке выводится дробь.
#
# Sample Input 1:
#
# 5
# Sample Output 1:
#
# 1/5
# 1/4
# 1/3
# 2/5
# 1/2
# 3/5
# 2/3
# 3/4
# 4/5
# Sample Input 2:
#
# 4
# Sample Output 2:
#
# 1/4
# 1/3
# 1/2
# 2/3
# 3/4

import math


def sort(arr):
    les = []
    eq = []
    gr = []

    if len(arr) > 1:
        pivot = arr[0][1]
        for x in arr:
            if x[1] < pivot:
                les.append(x)
            elif x[1] == pivot:
                eq.append(x)
            elif x[1] > pivot:
                gr.append(x)
        return sort(les) + eq + sort(gr)
    else:
        return arr


n = int(input())
arr = []
arr1 = []

for i in range(1, n + 1):
    for j in range(2, n + 1):
        if i < j and math.gcd(i, j) == 1 and i // j != 1:
            a = str(i) + "/" + str(j)
            b = i / j
            arr.append(a)
            arr.append(b)
            arr1.append(arr)
            arr = []

arr1 = sort(arr1)

for x in arr1:
    print(x[0])
