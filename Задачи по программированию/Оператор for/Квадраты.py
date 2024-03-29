# Квадраты
# Входные данные
#
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b.
#
# Выходные данные
#
# Выведите через пробел все числа на отрезке от a до b включительно, являющиеся полными квадратами. Если таких чисел нет, то ничего выводить не нужно.
#
# Sample Input:
#
# 2
# 8
# Sample Output:
#
# 4

a,b = [int(input()) for i in 'ab']

for i in range(a, b+1):
    for k in range(1, b+1):
        if i == k*k:
            print(i, end=' ');