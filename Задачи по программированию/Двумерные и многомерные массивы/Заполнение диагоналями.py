# Заполнение диагоналями
# Даны числа n и m. Создайте массив A[n][m] и заполните его, как показано на примере.
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
#   0  1  3  6 10 14 18 22 26 30
#   2  4  7 11 15 19 23 27 31 34
#   5  8 12 16 20 24 28 32 35 37
#   9 13 17 21 25 29 33 36 38 39

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

array = []

array = [[-1] * m for i in range(n)]

i = 0
x = -1
y = 1
d_column = -1
d_row = 1
s = y
t = 0

while True:
    while True:
        if 0 <= x + d_row < n and 0 <= y + d_column < m and array[x + d_row][y + d_column] == -1:
            x += d_row
            y += d_column
            array[x][y] = i
            i += 1
        elif 0 <= x + d_row < n and 0 <= y + d_column >= m:
            x = t + d_row
            y = m - 1
            array[x][y] = i
            t += 1
            i += 1
            break
        else:
            y = s + 1
            x = -1
            break
    s += 1
    if i == m * n:
        break

for i in range(n):
    for j in range(m):
        if checkDigit(array[i][j]) == 1:
            print('  ' + str(array[i][j]), end='')
        if checkDigit(array[i][j]) == 2:
            print(' ' + str(array[i][j]), end='')
        if checkDigit(array[i][j]) == 3:
            print(str(array[i][j]), end='')
    print()