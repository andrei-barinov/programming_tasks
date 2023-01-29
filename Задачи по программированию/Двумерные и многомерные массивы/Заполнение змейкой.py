# Заполнение змейкой
# Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).
#
# Входные данные
#
# Программа получает на вход два числа n и m.
#
# Выходные данные
#
# Программа должна вывести  полученный массив, отводя на вывод каждого числа ровно 3 символа.
#
# Sample Input:
#
# 4 10
# Sample Output:
#
#   0  1  2  3  4  5  6  7  8  9
#  19 18 17 16 15 14 13 12 11 10
#  20 21 22 23 24 25 26 27 28 29
#  39 38 37 36 35 34 33 32 31 30

def checkDigit(num):
    i = 0
    while True:
        i += 1
        num /= 10
        if num < 1:
            break
    return i

inArr = input().split(' ')

n = int(inArr[0])
m = int(inArr[1])

array=[]

array = [[-1] * m for i in range(n)]

i = 0
x = 0
y = -1
d_column = 1

while i <= n*m - 1:
    if 0 <= x < n and 0 <= y + d_column < m and array[x][y+d_column] == -1:
        y += d_column
        array[x][y] = i
        i += 1
    else:
        if d_column == 1:
            d_column = -1
            x += 1
            y += 1
        elif d_column == -1:
            d_column = 1
            x += 1
            y += -1

for i in range(n):
    for j in range(m):
        if checkDigit(array[i][j]) == 1:
            print('  ' + str(array[i][j]), end='')
        if checkDigit(array[i][j]) == 2:
            print(' ' + str(array[i][j]), end='')
        if checkDigit(array[i][j]) == 3:
            print(str(array[i][j]), end='')
    print()
