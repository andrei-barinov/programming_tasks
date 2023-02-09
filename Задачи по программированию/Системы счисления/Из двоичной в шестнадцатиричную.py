# Из двоичной в шестнадцатиричную
# Напишите программу, переводящую число из двоичной системы счисления в шестнадцатеричную.
#
# Входные данные
#
# Программа получает на вход строку, состоящую из нулей и единиц, длина которой не превосходит 1000 символов. Первый символ строки всегда единица. Данная строка является двоичной записью некоторого числа, которое необходимо записать в шестнадцатеричном виде и вывести с использованием цифр 0, ..., 9 и букв A, ..., F без лидирующих нулей.
#
# Выходные данные
#
# Выведите результат перевода.
#
# Sample Input:
#
# 101
# Sample Output:
#
# 5

def convertToDec(n):
    arr = list(map(int, list(n)))
    arr.reverse()

    s = 0
    for i in range(len(arr)):
        s += arr[i] * 2 ** i
    return s


def convertToHex(n):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    arr = []

    while True:
        d = n % 16
        if d > 9:
            arr.append(dic[d])
        else:
            arr.append(str(d))
        n = n // 16
        if n == 0:
            break

    arr.reverse()
    res = [str(x) for x in arr]

    return res


n = input()
num = convertToDec(n)
res = convertToHex(num)
print("".join(res))