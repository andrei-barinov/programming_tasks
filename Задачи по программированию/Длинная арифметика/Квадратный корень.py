# Квадратный корень
# Входные данные
#
# Дано число A, длина числа не превышает 250 знаков.
#
# Выходные данные
#
# Выведите такое наибольшее целое число X, что X2≤A.
#
# Sample Input:
#
# 8
# Sample Output:
#
# 2

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

n = int(input())

print(isqrt(n))