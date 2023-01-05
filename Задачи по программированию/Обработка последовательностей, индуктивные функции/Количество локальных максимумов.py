# Количество локальных максимумов
# Элемент последовательности называется локальным максимумом, если он строго больше предыдущего и последующего элемента последовательности. Первый и последний элемент последовательности не являются локальными максимумами.
#
# Дана последовательность натуральных чисел, признаком конца которой является число 0. Определите количество строгих локальных максимумов в этой последовательности.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
#
# Дана последовательность натуральных чисел, признаком конца которой является число 0.
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# 1
# 2
# 1
# 2
# 1
# 0
# Sample Output:
#
# 2

def getListOfNumbers(numbers: list):
    n = 0;
    arr = [];
    for i in range(2, len(numbers)):
        if (numbers[i - 2] < numbers[i - 1] > numbers[i]):
            n += 1;
            arr.append(n);

    n = 0;
    for i in range(2, len(numbers)):
        if (numbers[i - 2] > numbers[i - 1] < numbers[i]):
            n += 1;
            arr.append(n);

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

print(getMaximum(
    getListOfNumbers(numbers)
));