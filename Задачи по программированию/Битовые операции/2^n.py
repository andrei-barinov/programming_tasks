# 2^n
# Во всех упражнениях данного урока нельзя использовать арифметические операторы сложения, умножения, вычитания, деления. Вместо них нужно использовать побитовые операторы &, |, ~, ^, <<, >>. Входное число A не превышает 232-1 (если это не указано особо). Номера битов всегда задаются корректно, то есть принимают значения от 0 до 31. Ввод и вывод данных производится через стандартные потоки ввода-вывода.
#
# Напишите программу, вычисляющую заданную степень числа 2, используя битовые операции.
#
# Входные данные
#
# Дано число n<32.
#
# Выходные данные
#
# Выведите число 2n, то есть число, у которого n-й бит равен 1, а остальные – нули.
#
# Sample Input:
#
# 2
# Sample Output:
#
# 4

n = int(input())
print(1 << n)