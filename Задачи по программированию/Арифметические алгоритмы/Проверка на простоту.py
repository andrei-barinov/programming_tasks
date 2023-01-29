# Проверка на простоту
# Проверьте, является ли число простым.
#
# Входные данные
#
# Вводится одно натуральное число n не превышающее 2000000000 и не равное 1.
#
# Выходные данные
#
# Необходимо вывести  строку prime, если число простое, или composite, если число составное.
#
# Sample Input:
#
# 5
# Sample Output:
#
# prime

def checkNum(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())

if checkNum(n):
    print('prime')
else:
    print('composite')