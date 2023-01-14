# Наиболее удаленная точка
# Выведите координаты наиболее удаленной от начала координат точки.
#
# Входные данные
#
# Программа получает на вход набор точек на плоскости. Сначала задано количество точек n, затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки. Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие
# 1
# 0
# 3
# 10
# 3
#   по абсолютной величине.
#
# Выходные данные
#
# Выведите  координаты точки, наиболее удаленной от начала координат.
#
# Sample Input:
#
# 2
# 1 2
# 2 3
# Sample Output:
#
# 2 3

from math import sqrt;

def getResultArrFromString(arr):
    arr2 = [];
    for i in range(len(arr)):
        arr3 = arr[i].split(" ");
        result = getResultOfSqrt(arr3);
        arr3.append(result);
        arr2.append(arr3);
    return arr2;

def getResultOfSqrt(listOfPoint):
    result = sqrt(int(listOfPoint[0])*int(listOfPoint[0]) + int(listOfPoint[1])*int(listOfPoint[1]));
    return result;

n = int(input());
arr = [];

for i in range(n):
    string = input();
    arr.append(string);
arr2 = getResultArrFromString(arr);

max = arr2[0][2];
arr3 = arr2[0];
for i in range(1, len(arr2)):
    if arr2[i][2] > max:
        max = arr2[i][2];
        arr3 = arr2[i];

print(arr3[0], arr3[1]);