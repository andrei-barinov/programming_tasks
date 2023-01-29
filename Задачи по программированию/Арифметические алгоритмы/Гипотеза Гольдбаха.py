# Гипотеза Гольдбаха
# Гипотеза Гольдбаха (не доказанная до сих пор) утверждает, что любое четное число (кроме 2) можно представить в виде суммы двух простых чисел.
#
# Входные данные
#
# Программа получает на вход одно натуральное четное число n (3 < n < 2*105).
#
# Выходные данные
#
# Программа должна вывести два числа, разделенные пробелом (если числа не равны, сначала выводим меньшее, потом большее). Числа должны быть простыми и давать в сумме n.
#
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 2 2
# Sample Input 2:
#
# 6
# Sample Output 2:
#
# 3 3

def getSetEasyNum(n):
    a = []
    for i in range(n + 1):
        a.append(i)

    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = sorted(list(set(a)))
    a.remove(0)
    return a


n = int(input())

arr = getSetEasyNum(n)

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == n:
            print(arr[i], arr[j], end=' ')
            break
    if arr[i] + arr[j] == n:
        break