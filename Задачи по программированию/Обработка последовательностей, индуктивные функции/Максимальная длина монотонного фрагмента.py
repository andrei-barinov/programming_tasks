# Максимальная длина монотонного фрагмента
# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите наибольшую длину монотонного фрагмента последовательности (то есть такого фрагмента, где все элементы, кроме первого, либо больше предыдущего, либо меньше).
#
# Гарантируется, что в последовательности не менее двух чисел, отличных друг от друга.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
#
# Дана последовательность натуральных чисел, завершающаяся числом 0 (ноль не входит в последовательность).
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input 1:
#
# 1
# 7
# 7
# 9
# 1
# 0
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 0
# Sample Output 2:
#
# 7

def getListOfNumbers(numbers: list):
    n = 1;
    arr = [];
    for i in range(1, len(numbers)):
        if (numbers[i] > numbers[i - 1]):
            n += 1;
            if (i == len(numbers) - 1):
                arr.append(n);
                break;
        else:
            arr.append(n);
            n = 1;
    n = 1;
    for i in range(1, len(numbers)):
        if (numbers[i] < numbers[i - 1]):
            n += 1;
            if (i == len(numbers) - 1):
                arr.append(n);
                break;
        else:
            arr.append(n);
            n = 1;
    return arr;


def getMaximum(numbers):
    max = numbers[0];
    if len(numbers) == 1:
        return max;
    else:
        for i in range(1, len(numbers)):
            if numbers[i] > max:
                max = numbers[i];
    return max;


numbers = [];
while True:
    a = int(input());
    if a == 0:
        break;
    else:
        numbers.append(a);

print(
    getMaximum(
        getListOfNumbers(numbers)
    ));