# Больше своих соседей
# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов.
#
# Входные данные
#
# Вводится список чисел. Все числа списка находятся на одной строке.
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input 1:
#
# 1 2 3 4 5
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# 1 5 1 5 1
# Sample Output 2:
#
# 2

arr = input().split(" ");
j = 0;
for i in range(2, len(arr)):
    if ((int(arr[i]) < int(arr[i-1]) and int(arr[i-2]) < int(arr[i-1]))):
        j += 1;
print(j);