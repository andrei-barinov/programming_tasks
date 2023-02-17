# Universal convertor
# Напишите программу, переводящую запись числа между двумя произвольными системами счисления.
#
# Входные данные
#
# На вход программа получает три величины: n, A, k, где n и k — натуральные числа от 2 до 36, основания системы счисления, A — число, записанное в системе счисления с основанием n, A <
# 2
# 31
# 2
# 31
#  .
#
# Выходные данные
#
# Необходимо вывести значение A в системе счисления с основанием k без лидирующих нулей.
#
# Цифры записываются следующими символами: 0, 1, 2, ..., 9, A, B, C, ..., Z.
#
# Sample Input 1:
#
# 10
# 19
# 2
# Sample Output 1:
#
# 10011
# Sample Input 2:
#
# 10
# 32
# 3
# Sample Output 2:
#
# 1012

def convertAToDec(n, A):
    arr = list(str(A))

    d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
         'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
         'Y': 34, 'Z': 35}

    digitArr = []

    for x in arr:
        if str(x).isdigit():
            digitArr.append(int(x))
        else:
            digitArr.append(d[x])

    digitArr.reverse()

    s = 0
    for i in range(len(digitArr)):
        s += digitArr[i] * n ** i

    return s


def convertToK(k, A):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
           22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
           34: 'Y', 35: 'Z'}

    arr = []

    while True:
        d = A % k
        if d > 9:
            arr.append(dic[d])
        else:
            arr.append(str(d))
        A = A // k
        if A == 0:
            break

    arr.reverse()
    res = [str(x) for x in arr]

    return res


n = int(input())
A = input()
k = int(input())

A = convertAToDec(n, A)
numToK = convertToK(k, A)
print("".join(numToK))