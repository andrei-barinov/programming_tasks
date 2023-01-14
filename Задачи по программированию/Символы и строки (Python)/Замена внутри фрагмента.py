# Замена внутри фрагмента
# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
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
# In the Hole in tHe ground tHere lived a hobbit

string = input();

firstLetter = string.find('h');
lastLetter = string.rfind('h');

firstPart = string[:firstLetter+1];
lastPart = string[lastLetter:];
middlePart='';
middlePart = string[firstLetter+1:lastLetter].replace('h', 'H');

print(firstPart + middlePart + lastPart);