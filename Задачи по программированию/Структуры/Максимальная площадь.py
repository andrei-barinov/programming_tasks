# Максимальная площадь
# Среди исходных точек найдите три, образующие треугольник максимальной площади. Выведите данную площадь.
#
# Входные данные
#
# Программа получает на вход набор точек на плоскости. Сначала задано количество точек n (2 < n < 101), затем идет последовательность из n строк, каждая из которых содержит два числа: координаты точки. Все исходные координаты – целые числа, не превосходящие 103.
#
# Выходные данные
#
# Необходимо вывести найденную площадь в виде действительного числа.
#
# Sample Input:
#
# 4
# 0 0
# 0 1
# 1 0
# 1 1
# Sample Output:
#
# 0.5

def makeTriangle(arr):
    arr1 = [];
    arr2 = [];
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                a = ((int(arr[j][0]) - int(arr[i][0])) ** 2 + (int(arr[j][1]) - int(arr[i][1])) ** 2) ** 0.5;
                b = ((int(arr[k][0]) - int(arr[j][0])) ** 2 + (int(arr[k][1]) - int(arr[j][1])) ** 2) ** 0.5;
                c = ((int(arr[i][0]) - int(arr[k][0])) ** 2 + (int(arr[i][1]) - int(arr[k][1])) ** 2) ** 0.5;
                if (checkTriangle(a, b, c)):
                    arr1.append(a);
                    arr1.append(b);
                    arr1.append(c);
                    arr2.append(arr1);
                    arr1 = [];
    return arr2;


def checkTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a;


def calcSquareTriangle(arr):
    arr2 = [];
    for i in range(len(arr)):
        halfPerimeter = sum(arr[i]) / 2;
        s = (halfPerimeter * (halfPerimeter - arr[i][0]) * (halfPerimeter - arr[i][1]) * (
                    halfPerimeter - arr[i][2])) ** 0.5;
        arr2.append(round(s, 1));
    return arr2;


n = int(input());
arr = [];

for i in range(n):
    arr.append(input().split(" "));

arr2 = makeTriangle(arr);
arr3 = calcSquareTriangle(arr2);

print(max(arr3));