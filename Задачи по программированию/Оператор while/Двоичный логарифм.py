# Двоичный логарифм
# По данному натуральному числу N выведите такое наименьшее целое число k, что 2k≥N.
#
# Операцией возведения в степень пользоваться нельзя!
#
# Входные данные
#
# Вводится натуральное число N.
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# 7
# Sample Output:
#
# 3

n = int(input());
i = 0;
result = 1;

while True:
    if result >= n:
        print(i);
        break;
    i +=1;
    result *= 2;