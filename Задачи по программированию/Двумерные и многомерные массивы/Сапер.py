# Сапер
# Напишите программу, отображающую игровое поле для игры "Сапер".
#
# Входные данные
#
# Даны числа N и M (целые, положительные, не превышают 32) – количество строк и столбцов в поле соответственно, далее число W (целое, неотрицательное, не больше 1000) – количество мин на поле, далее следует W пар чисел, координаты мины на поле (первое число – строка, второе число – столбец).
#
# Выходные данные
#
# Требуется вывести на экран поле. Формат вывода указан в примере.
#
# Sample Input:
#
# 3 2
# 2
# 1 1
# 2 2
# Sample Output:
#
# * 2
# 2 *
# 1 1

n, m = map(int, input().split())
w = int(input())
result = [[0] * m for _ in range(n)]
for _ in range(w):
    i, j = map(int, input().split())
    result[i - 1][j - 1] = "*"

for i in range(n):
    for j in range(m):
        if result[i][j] == "*":
            continue
        mines = sum(result[i + di][j + dj] == "*" for di in range(-1, 2) for dj in range(-1, 2)
                    if 0 <= (i + di) < n and 0 <= (j + dj) < m)
        result[i][j] = mines

for i in range(n):
    print(" ".join(map(str, result[i])))