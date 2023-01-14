# Замена подстроки
# Дана строка. Замените в этой строке все цифры 1 на слово one.
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
# 1+1=2
# Sample Output:
#
# one+one=2

string = input();

newString = '';
newString = string.replace('1', 'one');

print(newString);