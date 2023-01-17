# Теорема Лагранжа
# Теорема Лагранжа утверждает, что любое натуральное число можно представить в виде суммы четырех точных квадратов. По данному числу n найдите такое представление: напечатайте от 1 до 4 натуральных чисел, квадраты которых дают в сумме данное число.
#
# Входные данные
#
# Программа получает на вход одно натуральное число n < 10000.
#
# Выходные данные
#
# Программа должна вывести от 1 до 4 натуральных чисел, квадраты которых дают в сумме данное число.
#
# Sample Input 1:
#
# 3
# Sample Output 1:
#
# 1 1 1
# Sample Input 2:
#
# 7
# Sample Output 2:
#
# 2 1 1 1

def checkSum(arr):
    sumArr = 0

    for i in arr:
        sumArr += i ** 2

    return sumArr

def searchIndexWithMinValue(arr):
    arrResult = []
    arrValueAndIndex = []
    minValue = arr[0]

    for i in range(1, 4):
        if arr[i] <= arr[i-1]:
            minValue = arr[i]
            arrValueAndIndex.append(arr[i])
            arrValueAndIndex.append(i)
            arrResult.append(arrValueAndIndex)
            arrValueAndIndex = []

    for i in range(len(arrResult)):
        if arrResult[i][0] == minValue:
            index = arrResult[i][1]
            break

    return index


n = int(input())

arr = [0, 0, 0, 0]

while True:
    if n == 0:
        break
    elif arr[0] == 0:
        arr[0] += 1
        if checkSum(arr) == n:
            break
    elif arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]:
        arr[0] += 1
        arr[1] = 0
        arr[2] = 0
        arr[3] = 0
        if checkSum(arr) == n:
            break
    elif arr[1] == arr[2] and arr[2] == arr[3]:
        arr[1] += 1
        arr[2] = 0
        arr[3] = 0
        if checkSum(arr) == n:
            break
    elif arr[2] == arr[3]:
        arr[2] += 1
        arr[3] = 0
        if checkSum(arr) == n:
            break
    else:
        index = searchIndexWithMinValue(arr)
        arr[index] += 1
        if checkSum(arr) == n:
            break

arrResult = []

if arr[0] == 0:
    print(0)
else:
    for x in arr:
        if x > 0:
            arrResult.append(x)

    print(*arrResult)




