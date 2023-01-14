# Личные дела
# Однажды, неловкая секретарша перепутала личные дела учащихся. Теперь их снова необходимо упорядочить сначала по классам, а внутри класса по фамилиям
#
# Входные данные
#
# В первой строке дано число N (1 ≤ N ≤ 1000) – количество личных дел. Далее для каждого из N учащихся следующие данные (каждое в своей строке): фамилия и имя, класс, дата рождения. Фамилия и имя – строки не более чем из 20 символов, класс – строка состоящая из числа (от 1 до 11) и латинской буквы (от "A" до "Z" ), дата рождения – дата в формате "ДД.ММ.ГГ" . Гарантируется, что внутри одного класса нет однофамильцев.
#
# Выходные данные
#
# В выходной файл требуется вывести N строк, в каждой из которых записаны данные по одному учащемуся. Строки должны быть упорядочены сначала по классам, а затем по фамилиям.
#
# Sample Input:
#
# 3
# Sidorov
# Sidor
# 9A
# 20.07.93
# Petrov
# Petr
# 9B
# 23.10.92
# Ivanov
# Ivan
# 9A
# 10.04.93
# Sample Output:
#
# 9A Ivanov Ivan 10.04.93
# 9A Sidorov Sidor 20.07.93
# 9B Petrov Petr 23.10.92

def makeArr(arr):
    arr1 = [];
    arr2 = [];
    for i in range(len(arr)):
        cl = list(arr[i][2]);
        if len(cl) == 2:
            arr1.append(int(cl[0]));
            arr1.append(cl[1]);
        else:
            st = cl[0] + cl[1];
            arr1.append(int(st));
            arr1.append(cl[2]);
        arr1.append(arr[i][0]);
        arr1.append(arr[i][1]);
        arr1.append(arr[i][3]);
        arr2.append(arr1);
        arr1 = [];
    return arr2;


def sortByNumberClass(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j];
            if arr[j][0] == arr[j + 1][0]:
                if sortByLetter(arr[j][1], arr[j + 1][1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j];
            if arr[j][0] == arr[j + 1][0] and arr[j][1] == arr[j + 1][1]:
                if sortBySurname(arr[j][2], arr[j + 1][2]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j];
    return arr;


def sortByLetter(letter1, letter2):
    return ord(letter1) > ord(letter2);


def sortBySurname(word1, word2):
    arr1 = list(word1);
    arr2 = list(word2);

    if (len(arr1) <= len(arr2)):
        for i in range(len(arr1)):
            if ord(word1[i]) > ord(word2[i]):
                return True;
            elif ord(word1[i]) == ord(word2[i]):
                continue;
            else:
                return False;
    if (len(arr2) < len(arr1)):
        for i in range(len(arr2)):
            if ord(word1[i]) > ord(word2[i]):
                return True;
            elif ord(word1[i]) == ord(word2[i]):
                continue;
            else:
                return False;


def printResult(arr):
    for i in range(len(arr)):
        print(str(arr[i][0]) + arr[i][1] + " " + arr[i][2] + " " + arr[i][3] + " " + arr[i][4])


n = int(input());
arr = [];
arr1 = [];

for i in range(n):
    for j in range(4):
        st = input();
        arr1.append(st);
    arr.append(arr1);
    arr1 = [];

arr2 = makeArr(arr);

arr3 = sortByNumberClass(arr2);

printResult(arr3);