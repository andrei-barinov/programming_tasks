# Быстрая проверка на простоту
# Входные данные
#
# Дано натуральное число N, 2 ≤ N ≤ 1018.
#
# Выходные данные
#
# Выведите YES, если число N является простым или NO, если число N является составным.
#
# Sample Input 1:
#
# 2
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# 3
# Sample Output 2:
#
# YES

def checkNum(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())

if checkNum(n):
    print('YES')
else:
    print('NO')