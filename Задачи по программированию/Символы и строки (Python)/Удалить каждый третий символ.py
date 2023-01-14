# Удалить каждый третий символ
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
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
# yton

string = input();

newString = '';

for i in range(len(string)):
    if i % 3 == 0:
        continue;
    newString += string[i];
print(newString);