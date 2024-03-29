# Наивный НОД
# Найдите НОД (наибольший общий делитель) двух чисел.
#
# Входные данные
#
# Вводятся два натуральных числа, не превосходящих 10000, разделенные пробелом.
#
# Выходные данные
#
# Выведите одно число - их наибольший общий делитель.
#
# Sample Input:
#
# 2 4
# Sample Output:
#
# 2

a, b = map(int, input().split(" "))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)