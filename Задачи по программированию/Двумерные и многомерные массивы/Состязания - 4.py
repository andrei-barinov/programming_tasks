# Состязания - 4
# В метании молота состязается n спортcменов. Каждый из них сделал mбросков. Победитель определяется по лучшему результату. Определите количество участников состязаний, которые разделили первое место, то есть определите количество строк в массиве, которые содержат значение, равное наибольшему.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести  одно число - количество победителей соревнования.
#
# Sample Input:
#
# 3 3
# 3 1 2
# 1 3 4
# 3 3 3
# Sample Output:
#
# 1

def makeIntFromStr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr


def findMaxEl(arr):
    arrCom = []
    arrForMaxEl = []
    maxEl = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > maxEl:
                maxEl = arr[i][j]
        arrForMaxEl.append(maxEl)
        arrCom.append(arrForMaxEl)
        arrForMaxEl = []
        maxEl = 0
    return arrCom


def findElWithMaxValue(arr):
    maxValue = 0
    for i in range(len(arr)):
        if arr[i][0] > maxValue:
            maxValue = arr[i][0]
    return maxValue


def findCountMaxValue(arr, maxValue):
    count = 0
    for i in range(len(arr)):
        if arr[i][0] == maxValue:
            count += 1
    return count


arrIn = input().split(" ")
n = int(arrIn[0])
m = int(arrIn[1])

arr = []

for i in range(n):
    arr.append(input().split(" "))

arr = makeIntFromStr(arr)
arrWithMaxEl = findMaxEl(arr)
maxValue = findElWithMaxValue(arrWithMaxEl)
count = findCountMaxValue(arrWithMaxEl, maxValue)

print(count)