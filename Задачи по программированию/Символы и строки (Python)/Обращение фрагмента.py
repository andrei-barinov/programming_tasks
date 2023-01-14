# Обращение фрагмента
# Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную между первым и последним появлением буквы h, в противоположном порядке.
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
# In th a devil ereht dnuorg eht ni eloh ehobbit

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

for i in range(lastLetter - 1, firstLetter, -1):
    newStr += string[i];
print(string[:firstLetter + 1] + newStr + string[lastLetter:]);