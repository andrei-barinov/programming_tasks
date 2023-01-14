# Встречалось ли число раньше
# Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
#
# Входные данные
#
# Вводится список чисел. Все числа списка находятся на одной строке.
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# 1 2 3 2 3 4
# Sample Output:
#
# NO
# NO
# NO
# YES
# YES
# NO

arr = input().split(" ");
s = set();

for i in range(len(arr)):
    if arr[i] in s:
        print("YES");
    else:
        print("NO");
    s.add(arr[i]);