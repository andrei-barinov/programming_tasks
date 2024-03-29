# Дружественные числа
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
#
# Входные данные
#
# Программа получает на вход одно натуральное число k, не превосходящее 105.
#
# Выходные данные
#
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает). В парах выводим сначала меньшее число, потом большее.
#
# Если таких пар нет - выводить ничего не нужно.
#
# Sample Input:
#
# 300
# Sample Output:
#
# 220 284

k = int(input())
amNum = [[220, 284], [1184, 1210], [2620, 2924], [5020, 5564], [6232, 6368], [10744, 10856], [12285, 14595], [17296, 18416], [63020, 76084], [66928, 66992], [67095, 71145], [69615, 87633], [79750, 88730]]

for i in range(len(amNum)):
    if amNum[i][0] <= k and amNum[i][1] <= k:
        print(*amNum[i])