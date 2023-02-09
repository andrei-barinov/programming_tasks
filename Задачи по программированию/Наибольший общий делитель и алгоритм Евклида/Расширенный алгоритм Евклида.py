# Расширенный алгоритм Евклида
# Даны натуральные числа a, b, c. Если уравнение ax+by=c имеет решения в целых числах, то выведите через пробел НОД(a,b), x и y (какое-нибудь решение). Если решения не существует, то выведите слово Impossible.
#
# Входные данные
#
# Входные данные - натуральные числа и не превышают по модулю 10000.
#
# Выходные данные
#
# Выведите ответ на задачу.

import math


def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd_ext(b, a % b)
    x, y = y, x - (a // b) * y
    return d, x, y


a, b, c = map(int, input().split())
d, x, y = gcd_ext(a, b)
if c % d != 0:
    print('Impossible')
else:
    cd = int(c / d)
    t = -(cd * x // int(b / d))
    x = cd * x + int(b / d) * t
    y = cd * y - int(a / d) * t
    if x < 0:
        x = cd * x + int(b / d)
        y = cd * y - int(a / d)
    print(math.gcd(a, b), x, y, sep=' ')