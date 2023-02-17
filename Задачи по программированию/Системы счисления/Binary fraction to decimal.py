# Binary fraction to decimal
# Переведите число из двоичной системы счисления в десятичную.
#
# Входные данные
#
# Дано число, представленное в виде двоичной дроби: запись длиной не более 30 символов, содержащая цифры 0 и 1 и, возможно, одну точку.
#
# Выходные данные
#
# Необходимо вывести данное число в виде десятичной дроби (тип переменной double с точностью не менее 12 знаков).
#
# Sample Input 1:
#
# 0.11
# Sample Output 1:
#
# 0.75
# Sample Input 2:
#
# 0.111
# Sample Output 2:
#
# 0.875

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


n = input()
if n.find('.') != -1:
    arr = n.split('.')
    if arr[0] == '0':
        c = convertToDec(arr[1])
        print(c)
    else:
        a = int(arr[0], 2)
        b = convertToDec(arr[1])
        c = float(a + b)
        print(c)
else:
    print(int(n, 2))