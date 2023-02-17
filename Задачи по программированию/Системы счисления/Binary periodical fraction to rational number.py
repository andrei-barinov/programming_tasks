# Binary periodical fraction to rational number
# Преобразуйте дробь.
#
# Входные данные
#
# Дана запись двоичной дроби, как в задаче "Binary periodical fraction to decimal", но в целых числах точки может не быть. Необходимо представить ее в виде несократимой рациональной дроби n/m.
#
# Выходные данные
#
# Программа должна вывести значения n и m через пробел.
#
# Sample Input 1:
#
# 0.1
# Sample Output 1:
#
# 1 2
# Sample Input 2:
#
# 0.01
# Sample Output 2:
#
# 1 4

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def convertToDec(n):
    arr = list(n)
    digitArr = []

    for x in arr:
        digitArr.append(int(x))

    s = 0
    for i in range(len(digitArr)):
        j = -(i + 1)
        s += digitArr[i] * 2 ** (j)
    return s


def convertNum(n):
    if n.find('.') != -1:
        arr = n.split('.')
        if arr[0] == '0':
            c = convertToDec(arr[1])
        else:
            a = int(arr[0], 2)
            b = convertToDec(arr[1])
            c = float(a + b)
    else:
        c = int(n, 2)
    return c


n = input()
p = str(convertNum(n))

if p.find('.') == -1:
    print(p, '1')
else:
    arr = p.split('.')
    if int(arr[0]) == 0:
        k = len(list(arr[1]))
        x = 10 ** k
        t = gcd(x, int(arr[1]))
        print(int(arr[1]) // t, x // t)
    else:
        k = len(list(arr[1]))
        x = 10 ** k
        f = int(arr[0]) * x + int(arr[1])
        t = gcd(f, int(arr[1]))
        print(f // t, x // t)