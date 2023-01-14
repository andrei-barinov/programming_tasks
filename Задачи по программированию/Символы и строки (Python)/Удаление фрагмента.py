# Удаление фрагмента
# Дана строка, в которой буква h встречается минимум два раза (это может быть как маленькая буква h, так и заглавная H). Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
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
# In the hole in the ground there lived a hobbit
# Sample Output:
#
# In tobbit

string = input();

a = string.find('h');
b = string.find('H');
c = string.rfind('h');
d = string.rfind('H');

if a == -1:
    firstLetter = b;
elif b == - 1:
    firstLetter = a;
elif a < b:
    firstLetter = a;
else:
    firstLetter = b;

if c == -1:
    lastLetter = d;
elif d == -1:
    lastLetter = c;
elif c > d:
    lastLetter = c;
else:
    lastLetter = d;

newStr = '';

for i in range(firstLetter):
    newStr += string[i];

for j in range(lastLetter + 1, len(string)):
    newStr += string[j];

print(newStr);