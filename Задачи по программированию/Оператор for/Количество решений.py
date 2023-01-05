# Количество решений
# Входные данные
#
# Вводятся 5 чисел: a, b, c, d и e.
#
# Выходные данные
#
# Найдите все целые решения уравнения ( ax3 + bx2 + cx + d ) / ( x - e ) = 0 на отрезке [0,1000] и выведите их количество.
#
# Sample Input:
#
# 1
# 2
# 3
# 4
# 5
# Sample Output:
#
# 0

a, b, c, d, e = [int(input()) for i in 'abcde'];

sum = 0;

for x in range(1001):
    if a * (x ** 3) + b * x * x + c * x + d == 0 and x - e != 0:
        sum += 1;

print(sum);