# Конвертирование
# Дана строка S, в которой выделили подстроку, состоящую из символов с i-го по j-й включительно (символы строки S нумеруются с единицы) и поменяли местами i-й символ с j-м, (i+1)-й с (j-1)-м и так далее (конвертировали подстроку). Выведите строку S после внесенных изменений.
#
# Входные данные
#
# В первой строке входного файла содержится строка S, длиной не более 1000 символов, во второй – числа i и  j (i ≤  j).
#
# Выходные данные
#
# В выходной файл выведите ответ на задачу.
#
# Sample Input:
#
# vjhoamkts
# 7 8
# Sample Output:
#
# vjhoamtks

string = input();
a, b = input().split(' ');
if int(a) == int(b):
    print(string);
else:
    secStr = '';
    for i in range(int(a) - 1, int(b)):
        secStr += string[i];
    thirdStr = '';
    for i in range(len(secStr)-1 , -1, -1):
        thirdStr += secStr[i];
    string = string.replace(secStr, thirdStr);
    print(string);