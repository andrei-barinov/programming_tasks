# Заполнение спиралью
# Дано число n. Создайте массив A[2*n+1][2*n+1] и заполните его по спирали, начиная с числа 0 в центральной клетке A[n+1][n+1]. Спираль выходит вверх, далее закручивается против часовой стрелки.
#
# Входные данные
#
# Программа получает на вход одно число n.
#
# Выходные данные
#
# Программа должна вывести  полученный массив, отводя на вывод каждого числа ровно 3 символа.
#
# Sample Input:
#
# 2
# Sample Output:
#
#  12 11 10  9 24
#  13  2  1  8 23
#  14  3  0  7 22
#  15  4  5  6 21
#  16 17 18 19 20

n = int(input())


def checkDigit(num):
    i = 0
    while True:
        i += 1
        num /= 10
        if num < 1:
            break
    return i


array = []
for i in range(2 * n + 1):
    array.append([])
    for j in range(2 * n + 1):
        array[i].append(0)
# print(array)

add_num = (2 * n + 1) ** 2 - 1
for i in range(0, n):
    for j in range(i, 2 * n + 1 - i):
        array[j][2 * n - i] = add_num
        add_num -= 1
    for j in range(i, 2 * n - i):
        array[2 * n - i][2 * n - 1 - j] = add_num
        add_num -= 1
    for j in range(i, 2 * n - i):
        array[2 * n - 1 - j][i] = add_num
        add_num -= 1
    for j in range(i, 2 * n - i - 1):
        array[i][j + 1] = add_num
        add_num -= 1

for i in range(len(array)):
    for j in range(len(array)):
        if checkDigit(array[i][j]) == 1:
            print('  ' + str(array[i][j]), end='')
        if checkDigit(array[i][j]) == 2:
            print(' ' + str(array[i][j]), end='')
        if checkDigit(array[i][j]) == 3:
            print(str(array[i][j]), end='')
    print()
