# Сумма последовательности - 2
# Найдите сумму последовательности натуральных чисел, если признаком окончания конца последовательности является два подряд идущих числа 0.
#
# Числа, следующие после двух подряд идущих нулей считывать не нужно.
#
# Входные данные
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# 1
# 0
# 7
# 0
# 9
# 0
# 0
# Sample Output:
#
# 17

sum = 0;
b = 1;
while True:
    a = int(input());
    if a == 0 and a == b: break;
    else:
        b = a;
        sum += a;
print(sum);