# Сортировка точек
# Выведите все исходные точки в порядке возрастания их расстояний от начала координат.
#
# Входные данные
#
# Программа получает на вход набор точек на плоскости. Сначала задано количество точек n, затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки. Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие 103.
#
# Выходные данные
#
# Необходимо вывести  все исходные точки в порядке возрастания их расстояний от начала координат. Программа выводит только координаты точек, их количество выводить не надо. Если две точки находятся на одинаковом расстоянии от начала координат - выводить их в том порядке, в котором они вводятся.
#
# Sample Input:
#
# 2
# 1 2
# 2 3
# Sample Output:
#
# 1 2
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

def sortArr(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j][2] > arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j];
    return arr;

n = int(input());
arr = [];

for i in range(n):
    string = input();
    arr.append(string);
arr2 = getResultArrFromString(arr);

arr3 = sortArr(arr2);

for i in range(len(arr2)):
    print(arr3[i][0] + " " + arr3[i][1]);