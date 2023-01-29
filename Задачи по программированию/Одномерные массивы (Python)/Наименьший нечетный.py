# Наименьший нечетный
# Выведите значение наименьшего нечетного элемента списка, а если в списке нет нечетных элементов - выведите число 0.
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
# 0 1 2 3 4
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# 2 4 6 8 10
# Sample Output 2:
#
# 0

arr = input().split(" ");
othArr = [];

for i in range(len(arr)):
    if int(arr[i]) % 2 == 1:
        othArr.append(int(arr[i]));
if len(othArr) != 0:
    print(min(othArr));
else: print(0);