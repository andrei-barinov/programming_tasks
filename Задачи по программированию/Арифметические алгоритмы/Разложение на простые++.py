# Разложение на простые++
# Требуется разложить целое число N на простые множители и вывести результат в порядке возрастания.
#
# Входные данные
#
# Программе дано число N (2 ≤ N ≤ 109).
#
# Выходные данные
#
# Вывести разложение N на простые множители.
#
# Sample Input 1:
#
# 2
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 1008
# Sample Output 2:
#
# 2^4*3^2*7

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

n = int(input())

arr = Factor(n)


arr1 = []
arr2 = []
arr3 = sorted(list(set(arr)))

for i in range(len(arr3)):
    arr1.append(arr3[i])
    arr1.append(arr.count(arr3[i]))
    arr2.append(arr1)
    arr1 = []

for i in range(len(arr2)):
    if i == len(arr2)-1:
        if arr2[i][1] == 1:
            print(str(arr2[i][0]))
        else:
            print(str(arr2[i][0]) + '^' + str(arr2[i][1]))
    else:
        if arr2[i][1] == 1:
            print(str(arr2[i][0]) + '*', end='')
        else:
            print(str(arr2[i][0]) + '^' + str(arr2[i][1]) + '*', end='')