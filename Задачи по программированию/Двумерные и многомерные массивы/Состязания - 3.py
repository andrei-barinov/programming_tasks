# Состязания - 3
# В метании молота состязается n спортcменов. Каждый из них сделал mбросков. Побеждает спортсмен, у которого максимален наилучший бросок. Если таких несколько, то из них побеждает тот, у которого наилучшая сумма результатов по всем попыткам. Если и таких несколько, победителем считается спортсмен с минимальным номером. Определите номер победителя соревнований.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести одно число - номер победителя соревнований. Не забудьте, что  строки  (спортсмены) нумеруются с 0.
#
# Sample Input:
#
# 3 3
# 1 2 7
# 1 3 5
# 4 1 6
# Sample Output:
#
# 0

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


def getSumEl(arr, arrWithMaxEl):
    sumEl = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            sumEl += arr[i][j]
        arrWithMaxEl[i].append(sumEl)
        sumEl = 0
        arrWithMaxEl[i].append(i)
    return arrWithMaxEl


def findMaxElFromArrWithMaxEl(arr):
    maxEl = 0
    for i in range(len(arr)):
        if arr[i][0] > maxEl:
            maxEl = arr[i][0]
    return maxEl


def makeCommonArr(arrWithMaxElAndWithSumEl, maxEl):
    commonArr = []
    for i in range(len(arrWithMaxElAndWithSumEl)):
        if arrWithMaxElAndWithSumEl[i][0] == maxEl:
            commonArr.append(arrWithMaxElAndWithSumEl[i])
    return commonArr


def findMaxSumFromCommonArr(arr):
    maxSum = 0
    for i in range(len(arr)):
        if arr[i][1] > maxSum:
            maxSum = arr[i][1]
    return maxSum


def makeCommonArrWithMaxSum(arr, maxSum):
    commonArr = []
    for i in range(len(arr)):
        if arr[i][1] == maxSum:
            commonArr.append(arr[i])
    return commonArr


arrIn = input().split(" ")
n = int(arrIn[0])
m = int(arrIn[1])

arr = []

for i in range(n):
    arr.append(input().split(" "))

arr = makeIntFromStr(arr)
arrWithMaxEl = findMaxEl(arr)
arrWithMaxElAndWithSumEl = getSumEl(arr, arrWithMaxEl)
maxEl = findMaxElFromArrWithMaxEl(arrWithMaxElAndWithSumEl)
commonArr = makeCommonArr(arrWithMaxElAndWithSumEl, maxEl)
maxSum = findMaxSumFromCommonArr(commonArr)
commonArr2 = makeCommonArrWithMaxSum(commonArr, maxSum)

print(commonArr2[0][2])