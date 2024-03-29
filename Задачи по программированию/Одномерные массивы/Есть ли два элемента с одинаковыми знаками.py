# Есть ли два элемента с одинаковыми знаками
# Дан массив, состоящий из целых чисел. Напишите программу, которая определяет, есть ли в массиве пара соседних элементов с одинаковыми знаками.
#
# Входные данные
#
# Сначала задано число N — количество элементов в массиве (1 ≤ N ≤ 10000). Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Выходные данные
#
# Необходимо вывести слово YES, если существует пара соседних элементов с одинаковыми знаками. В противном случае следует вывести слово NO.
#
# Sample Input:
#
# 5
# 1 -3 4 -2 1
# Sample Output:
#
# NO

n = int(input());
arr = input().split(" ");
j = False;
for i in range(1, n):
    if (int(arr[i-1]) >0 and int(arr[i]) > 0) or (int(arr[i-1]) <0 and int(arr[i]) < 0):
        j = True;
        break;
if j:
    print("YES");
else:
    print("NO");
