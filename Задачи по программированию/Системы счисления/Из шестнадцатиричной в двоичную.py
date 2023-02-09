# Из шестнадцатиричной в двоичную
# Напишите программу, переводящую число из шестнадцатеричной системы счисления в двоичную.
#
# Входные данные
#
# Программа получает на вход строку, состоящую из цифр 0, ..., 9 и букв A, ..., F, являющуюся записью некоторого 16-ричного целого числа. Длина строки не превосходит 50 символов, первый символ в строке не равен 0. Необходимо вывести запись этого числа в двоичном виде без лидирующих нулей.
#
# Выходные данные
#
# Выведите результат перевода.
#
# Sample Input:
#
# 14
# Sample Output:
#
# 10100

def convertToDec(n):
    arr = list(n)
    d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    digitArr = []

    for x in arr:
        if str(x).isdigit():
            digitArr.append(int(x))
        else:
            digitArr.append(d[x])

    digitArr.reverse()

    s = 0
    for i in range(len(digitArr)):
        s += digitArr[i] * 16 ** i

    return s


def convertToDouble(n):
    arr = []

    while True:
        d = n % 2
        arr.append(d)
        n = n // 2
        if n == 0:
            break

    arr.reverse()
    res = [str(x) for x in arr]

    return res


n = input()

num = convertToDec(n)
numDouble = convertToDouble(num)

print("".join(numDouble))
