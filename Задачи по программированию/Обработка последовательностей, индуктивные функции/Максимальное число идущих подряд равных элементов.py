# Максимальное число идущих подряд равных элементов
# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу. Если все элементы разные, максимальным числом будет 1.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
#
# Дана последовательность натуральных чисел, завершающаяся числом 0.
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
# 0
# Sample Output 2:
#
# 1

def getListOfNumbers(numbers: list):
    n = 1;
    arr = [];
    if len(numbers) == 1:
        arr.append(1);
        return arr;
    elif len(numbers) == 2:
        if (numbers[0] == numbers[1]):
            arr.append(2)
            return arr;
    else:
        for i in range(1, len(numbers)):
            if (numbers[i] == numbers[i - 1]):
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
        getListOfNumbers(numbers)));