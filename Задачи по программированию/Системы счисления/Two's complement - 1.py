# Two's complement - 1
# Напишите программу, которая по данным числам A и n записывает представление числа A в n-разрядном двоичном дополнительном коде.
#
# Входные данные
#
# Первая строка входных данных содержит число A, вторая строка – число n, при этом    2 ≤ n ≤ 16,    −2 n−1 ≤ A ≤ 2 n−1−1 .
#
# Выходные данные
#
# Программа должна вывести строку из n символов, содержащих запись числа A в n-разрядном двоичном дополнительном коде, первый символ – старший знаковый разряд.
#
# Sample Input 1:
#
# 3
# 8
# Sample Output 1:
#
# 00000011
# Sample Input 2:
#
# 57
# 8
# Sample Output 2:
#
# 00111001

def convertPositiveToDouble(A, n):
    arr = []

    while True:
        d = A % 2
        arr.append(d)
        A = A // 2
        if A == 0:
            break

    m = n - len(arr)

    if m > 0:
        for i in range(m):
            arr.append('0')

    arr.reverse()
    res = [str(x) for x in arr]

    return res


def convertNegativeToDouble(A, n):
    x = bin(~A)[2:]

    arr = list(x)
    arr.reverse()

    m = n - len(arr)

    if m > 0:
        for i in range(m):
            arr.append("0")

    arr.reverse()
    newArr = []

    for i in range(len(arr)):
        if i == 0:
            newArr.append("1")
            continue
        elif arr[i] == "0":
            newArr.append("1")
        else:
            newArr.append("0")

    return newArr


A = int(input())
n = int(input())

if A >= 0:
    print("".join(convertPositiveToDouble(A, n)))
else:
    print("".join(convertNegativeToDouble(A, n)))