# Ферзи
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#
# Входные данные
#
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
#
# Выходные данные
#
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
#
# Sample Input 1:
#
# 1 7
# 2 4
# 3 2
# 4 8
# 5 6
# 6 1
# 7 3
# 8 5
# Sample Output 1:
#
# NO
# Sample Input 2:
#
# 1 8
# 2 7
# 3 6
# 4 5
# 5 4
# 6 3
# 7 2
# 8 1
# Sample Output 2:
#
# YES

arr = []
arr2 = []
tmp = 0

for i in range(8):
    arr2 = input().split(" ")
    arr.append(arr2)

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        if arr[i][0] == arr[j][0]:
            tmp = 1
            break
        if arr[i][1] == arr[j][1]:
            tmp = 1
            break
        if (int(arr[i][0]) / int(arr[i][1]) == 1.0) and (int(arr[j][0]) / int(arr[j][1]) == 1.0):
            tmp = 1
            break
        if int(arr[i][0]) + int(arr[i][1]) == int(arr[j][0]) + int(arr[j][1]):
            tmp = 1
            break
        if int(arr[i][0]) - int(arr[i][1]) == int(arr[j][0]) - int(arr[j][1]):
            tmp = 1
            break
        if int(arr[i][0]) + int(arr[i][1]) == int(arr[j][0]) + int(arr[j][1]):
            tmp = 1
            break
    if tmp == 1:
        break
if tmp == 1:
    print('YES')
else:
    print('NO')