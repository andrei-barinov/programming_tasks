# Удаление символа
# Дана строка. Удалите из этой строки все символы @.
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
# Bilbo.Baggins@bagend.hobbiton.shire.me
# Sample Output:
#
# Bilbo.Bagginsbagend.hobbiton.shire.me

string = input();

newString = '';
newString = string.replace('@', '');

print(newString);
