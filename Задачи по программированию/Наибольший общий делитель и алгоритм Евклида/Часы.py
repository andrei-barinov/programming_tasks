# Часы
# В марсианских сутках N часов. У марсиан Ятеп и Ашам есть часы со стрелками, которые работают почти так же, как земные – большая стрелка делает один оборот в час, а маленькая – один оборот в сутки. Ятеп и Ашам поссорились и решили не разговаривать, пока стрелки часов не совпадут. Определите точный момент времени, когда это случится.
#
# Входные данные
#
# Во входном файле задано число тестов K (0 ≤ K<
# 1
# 0
# 4
# 10
# 4
#  ), далее для каждого теста указаны целые числа N, A, B и C (1<N<
# 1
# 0
# 9
# 10
# 9
#  , 0 ≤ A < N, 0 ≤ B < C <
# 1
# 0
# 9
# 10
# 9
#  ). Числа A, B и C означают, что Ятеп и Ашам поссорились в A+B/C часов.
#
# Выходные данные
#
# Для каждого теста выведите искомое время в том же формате: числа A, B и C, такие, что искомое время равно A+B/C (0 ≤ A < N, 0 ≤ B < C, дробь B/C – несократимая).
#
# Sample Input:
#
# 2
# 12 11 0 1
# 12 0 0 1
# Sample Output:
#
# 0 0 1
# 1 1 11

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


for _ in range(int(input())):
    n, a1, b1, c1 = map(int, input().split())
    if n > 2:
        if b1 * (n - 1) >= a1 * c1:
            a1 += 1
        if a1 >= n - 1:
            a1, b1, c1 = 0, 0, 1
        else:
            k = gcd(a1, n - 1)
            b1 = a1 // k
            c1 = (n - 1) // k
    elif n == 2:
        a1, b1, c1 = 0, 0, 1
    print(a1, b1, c1)