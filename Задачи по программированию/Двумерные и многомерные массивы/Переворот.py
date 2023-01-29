# Переворот
# Дан массив N × M. Требуется повернуть его по часовой стрелке на 90 градусов.
#
# Входные данные
#
# На первой строке даны натуральные числа N и M (1 ≤ N, M ≤ 50). На следующих N строках записано по M неотрицательных чисел, не превышающих 109 – сам массив.
#
# Выходные данные
#
# Выведите повернутый массив в формате входных данных.
#
# Sample Input:
#
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# Sample Output:
#
# 9 5 1
# 10 6 2
# 11 7 3
# 12 8 4

def makeIntFromStr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr

def makeNewArr(arr):
    arr1 = []
    arr2 = []
    k = 0
    while k < len(arr[0]):
        for i in range(len(arr)-1, -1, -1):
            arr1.append(arr[i][k])
        arr2.append(arr1)
        arr1 = []
        k += 1
    return arr2

inArr = input().split(' ')

n = int(inArr[0])
m = int(inArr[1])

arr = []
arr2 = []

for i in range(n):
    arr.append(input().split(" "))

arr = makeIntFromStr(arr)
arr2 = makeNewArr(arr)

for i in range(m):
    print(" ".join(map(str, arr2[i])))