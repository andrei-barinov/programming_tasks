# Делаем срезы
# Выполните разбор строки, согласно приведенным правилам.
#
# Входные данные
#
# Дана строка.
#
# Выходные данные
#
# Сначала выведите третий символ этой строки.
#
# Во второй строке выведите предпоследний символ этой строки.
#
# В третьей строке выведите первые пять символов этой строки.
#
# В четвертой строке выведите всю строку, кроме последних двух символов.
#
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
#
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
#
# В седьмой строке выведите все символы в обратном порядке.
#
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
#
# В девятой строке выведите длину данной строки.
#
# Sample Input:
#
# Abrakadabra
# Sample Output:
#
# r
# r
# Abrak
# Abrakadab
# Arkdba
# baaar
# arbadakarbA
# abdkrA
# 11

string = input();
print(string[2]);
print(string[-2]);
print(string[:5]);
print(string[:-2]);
print(string[::2]);
print(string[1::2]);
print(string[::-1]);
print(string[::-2]);
print(len(string));
