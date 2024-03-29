# Полярные единички
# Программист на Северном полюсе работал за компьютером в варежках и поэтому мог набирать только 0 и 1, а клавиша 0 запала. Сможет ли он набрать число, состоящее только из единиц и при этом кратное заданному N?
#
# Входные данные
#
# Программе дано число N (1 ≤ N ≤ 106).
#
# Выходные данные
#
# Вывести минимальное число, удовлетворяющее требованию, или "NO" , если такого числа не существует.
#
# Sample Input 1:
#
# 100
# Sample Output 1:
#
# NO
# Sample Input 2:
#
# 57
# Sample Output 2:
#
# 111111111111111111

n = int(input())

if n%2 == 0:
    print('NO')
elif set(str(n)) == {'1'}:
    print(n)
else:
    x = 0
    for i in range(1, n + 2):
        x = (10 * x + 1) % n
        if x == 0:
            for j in range(i):
                print(1, end='')
            break