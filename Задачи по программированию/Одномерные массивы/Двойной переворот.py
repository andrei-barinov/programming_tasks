# Двойной переворот
# Дана последовательность натуральных чисел 1, 2, 3, ..., N (1 ≤ N ≤ 1000). Необходимо сначала расположить в обратном порядке часть этой последовательности от элемента с номером A до элемента с номером B, а затем от C до D (A < B; C < D; 1 ≤ A, B, C, D ≤ N).
#
# Входные данные
#
# Вводятся натуральные числа числа N, A, B, C, D.
#
# Выходные данные
#
# Требуется вывести полученную последовательность. Числа следует выводить через пробел.
#
# Sample Input:
#
# 9 2 5 6 9
# Sample Output:
#
# 1 5 4 3 2 9 8 7 6

def getArrResult(arr, a, b):
    firstArr = [];

    for i in range(a - 1, b):
        firstArr.append(arr[i]);

    for j in range(len(firstArr)):
        for i in range(1, len(firstArr) - j):
            firstArr[i], firstArr[i - 1] = firstArr[i - 1], firstArr[i];

    beginArrFirst = [];

    for i in range(a - 1):
        beginArrFirst.append(arr[i]);

    endArrFirst = [];

    for i in range(b, len(arr)):
        endArrFirst.append(arr[i]);

    resultArrFirst = [];

    for i in range(len(beginArrFirst)):
        resultArrFirst.append(beginArrFirst[i]);
    for i in range(len(firstArr)):
        resultArrFirst.append(firstArr[i]);
    for i in range(len(endArrFirst)):
        resultArrFirst.append(endArrFirst[i]);

    return resultArrFirst;


arr = input().split(" ");
n = int(arr[0]);
a = int(arr[1]);
b = int(arr[2]);
c = int(arr[3]);
d = int(arr[4]);

newArr = [];

for i in range(1, n + 1):
    newArr.append(i);

result1 = getArrResult(newArr, a, b);
result2 = getArrResult(result1, c, d);

print(" ".join(map(str, result2)));