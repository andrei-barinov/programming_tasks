# Двоичная запись
# Дано натуральное число N. Выведите его представление в двоичном виде в обратном порядке.
#
# Входные данные
#
# Задано единственное число N
#
# Выходные данные
#
# Необходимо вывести требуемое представление числа N.
#
# Sample Input:
#
# 6
# Sample Output:
#
# 011

n = int(input());
while n != 0:
    print(n % 2, end='');
    n //= 2;