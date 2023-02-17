# N^N mod 10^P
# Входные данные
#
# Даны два числа N и P (1≤N≤109, 1≤P≤100).
#
# Выходные данные
#
# Вычислите NN mod 10P.
#
# Sample Input:
#
# 5 3
# Sample Output:
#
# 125

n, p = map(int, input().split(' '))

print(pow(n, n, pow(10, p)))