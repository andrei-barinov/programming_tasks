# Трое лучших
# Определите трех учащихся с наилучшим средним баллом по трем предметам. Выведите фамилии и имена этих учащихся. Если при этом у нескольких учащихся средний балл совпадает со средним баллом учащегося, "занявшего 3-е место", то необходимо вывести их всех.
#
# Входные данные
#
# Заданы сначала количество учащихся n, затем n строк, каждая из которых содержит фамилию, имя и три числа (оценки по трем предметам: математике, физике, информатике). Данные в строке разделены одним пробелом. Оценки принимают значение от 1 до 5.
#
# Выходные данные
#
# Необходимо вывести пары фамилия-имя по одной на строке, разделяя фамилию и имя одним пробелом. Выводить оценки не нужно. Порядок вывода должен быть таким же, как в исходных данных.
#
# Sample Input 1:
#
# 3
# Yakovlev Ivan 5 5 5
# Yapryntsev Aleksey 5 5 5
# Kozlov Georgiy 5 5 5
# Sample Output 1:
#
# Yakovlev Ivan
# Yapryntsev Aleksey
# Kozlov Georgiy
# Sample Input 2:
#
# 10
# Krasnov Ivan 3 3 3
# Shusha Andrey 1 2 4
# Ivanov Petr 2 5 3
# Markov Valeriy 2 3 5
# Petrov Sergey 1 2 1
# Garkov Vanya 4 5 1
# Radov Stepan 3 2 1
# Korod Zenya 1 5 5
# Solovey Gavrila 5 5 1
# Zubok Anton 3 5 4
# Sample Output 2:
#
# Korod Zenya
# Solovey Gavrila
# Zubok Anton

def makeArray(st):
    arr1 = [];
    sumMark = (int(st[2]) + int(st[3]) + int(st[4]));
    arr1.append(st[0] + " " + st[1]);
    arr1.append(sumMark);
    arr1.append(i);
    return arr1;


def sortArray(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr;


def getResultList(arr):
    arr1 = [];
    arr1.extend((arr[0], arr[1], arr[2]));
    for i in range(3, len(arr)):
        if arr[i][1] == arr[2][1]:
            arr1.append(arr[i]);
    return arr1;


def sortGetResultList(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][2] > arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr;


n = int(input());
arr = [];

for i in range(n):
    st = input().split(" ");
    arr.append(makeArray(st));

arr2 = sortArray(arr);

if len(arr2) > 3:
    arr3 = getResultList(arr2);
else:
    arr3 = arr2;

arr4 = sortGetResultList(arr3);

for i in range(len(arr4)):
    print(arr4[i][0]);