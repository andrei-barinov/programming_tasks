# Сумма двух кубов
# Представьте данное число n в виде суммы двух кубов.
#
# Входные данные
#
# Программа получает на вход одно натуральное число n (n <= 1028).
#
# Выходные данные
#
# Программа должна вывести 2 целых положительных числа, сумма кубов которых равна n (выводить в порядке возрастания). Если это невозможно, выведите строку impossible.
#
# Sample Input 1:
#
# 2
# Sample Output 1:
#
# 1 1
# Sample Input 2:
#
# 3
# Sample Output 2:
#
# impossible

def getCub(n):
    i = 0
    while True:
        i += 1
        value = i**3
        if value >= n:
            break
    return i

n = int(input())

k = getCub(n)
c = -1
d = -1

for i in range(1, k+1):
    for j in range(1, k+1):
        if i**3+j**3 == n:
            c = i
            d = j

if c == -1:
    print('impossible')
else:
    if c > d:
        print(d, c, end = ' ')
    else:
        print(c, d, end = ' ')