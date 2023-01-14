# Дублирование фрагмента
# Дана строка, в которой буква h встречается как минимум два раза. Повторите последовательность символов, заключенную между первым и последним появлением буквы h два раза, сами буквы h повторять не надо.
#
# Имейте ввиду, в тексте могут встречаться заглавные буквы H.
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
# In the hole in the ground there lived a e hole in the ground there lived a hobbit

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
firstPart = string[:firstLetter + 1];
lastPart = string[lastLetter:];

for i in range(firstLetter + 1, lastLetter):
    newStr += string[i];
print(firstPart + 2 * newStr + lastPart);