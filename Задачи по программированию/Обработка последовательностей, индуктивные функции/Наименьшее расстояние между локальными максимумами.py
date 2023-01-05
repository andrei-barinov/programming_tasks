# Наименьшее расстояние между локальными максимумами
# Определите наименьшее расстояние между двумя локальными максимумами последовательности натуральных чисел, завершающейся числом 0. Если в последовательности нет двух локальных максимумов, выведите число 0.
#
# Входные данные
#
# Дана последовательность натуральных чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит)
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# ЗЫ: Расстоянием считается количество пробелов между элементами. Пример на скриншоте ниже:
#
#
#
# Sample Input:
#
# 1
# 2
# 1
# 1
# 2
# 1
# 2
# 1
# 0
# Sample Output:
#
# 2

def getListOfIndexes(numbers: list):
    n = 0;
    arr = [];
    for i in range(2, len(numbers)):
        if (numbers[i - 2] < numbers[i - 1] > numbers[i]):
            arr.append(i - 1);
    return arr;


def getDifference(numbers):
    if len(numbers) < 2:
        return 0;
    min = 100000;
    for i in range(1, len(numbers)):
        x = numbers[i] - numbers[i - 1];
        if x < min:
            min = x;
    return min;


numbers = [];
while True:
    a = int(input());
    if a == 0:
        break;
    else:
        numbers.append(a);

print(getDifference(
    getListOfIndexes(numbers)
));
