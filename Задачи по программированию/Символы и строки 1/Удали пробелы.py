# Удали пробелы
# Дана строка, Вам требуется преобразовать все идущие подряд пробелы в один. Если пробелы есть в начале и в конце строки - их нужно убрать.
#
# Входные данные
#
# Длина строки не превосходит 1000.
#
# Выходные данные
#
# Выведите измененную строку.
#
# Sample Input:
#
# nz d urp lren s bwz  boom  t a   j    ho    vi
# Sample Output:
#
# nz d urp lren s bwz boom t a j ho vi

string = input();
string = string.strip();
secStr = '';
for i in range(len(string)):
    if string[i] == ' ' and string[i - 1] == ' ':
        continue;
    else:
        secStr += string[i];
print(secStr);