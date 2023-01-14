# Вставка символов
# Дана строка. Получите новую строку, вставив между двумя символами исходной строки символ *. Выведите полученную строку.
#
# Входные данные
#
# Вводится строка.
#
# Выходные данные
#
# Выведите ответ на задачу.
#
# Sample Input:
#
# Python
# Sample Output:
#
# P*y*t*h*o*n

string = input();

newString = '';

for i in range(len(string)):
    newString += string[i]
    if i == len(string)-1:
        break;
    else:
        newString += '*';

print(newString);