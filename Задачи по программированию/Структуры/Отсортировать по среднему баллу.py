# Отсортировать по среднему баллу
# Выведите фамилии и имена учащихся в порядке убывания их среднего балла.
#
# Входные данные
#
# Заданы сначала количество учащихся n, затем n строк, каждая из которых содержит фамилию, имя и три числа (оценки по трем предметам: математике, физике, информатике). Данные в строке разделены одним пробелом. Оценки принимают значение от 1 до 5.
#
# Общее число учащихся не превосходит 100001.
#
# Выходные данные
#
# Необходимо вывести пары фамилия-имя по одной на строке, разделяя фамилию и имя одним пробелом. Выводить оценки не нужно. Если несколько учащихся имеют одинаковые средние баллы, то их нужно выводить в порядке, заданном во входных данных.
#
# Sample Input:
#
# 2
# Markov Valeriy 1 1 1
# Ivanov Ivan 2 2 2
# Sample Output:
#
# Ivanov Ivan
# Markov Valeriy

def makeArray(st):
    arr1 = [];
    sumMark = (int(st[2]) + int(st[3]) + int(st[4]));
    arr1.append(st[0] + " " + st[1]);
    arr1.append(sumMark);
    return arr1;


def sortArray(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr;


n = int(input());
arr = [];

for i in range(n):
    st = input().split(" ");
    arr.append(makeArray(st));

arr2 = sortArray(arr);

for i in range(len(arr2)):
    print(arr2[i][0]);