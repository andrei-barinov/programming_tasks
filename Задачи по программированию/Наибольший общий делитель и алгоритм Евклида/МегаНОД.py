# МегаНОД
# Дано N чисел. Найти самое большое число, на которое делятся все N чисел.
#
# Входные данные
#
# В первой строке дано число N. Во второй строке даны через пробел N чисел (1 <= N <= 1000).
#
# Выходные данные
#
# Выведите искомое число.
#
# Sample Input 1:
#
# 1
# 3
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 3
# 9 15 22
# Sample Output 2:
#
# 1

from math import gcd
from functools import reduce

n = int(input())
arr = list(map(int, input().split(" ")))

a = reduce(gcd, arr)

print(a)