# Шифр Юлия
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфавиту через K позиций по кругу. Необходимо по заданной шифровке определить исходный текст.
#
# Входные данные
#
# В первой строке дана шифровка, состоящая из заглавных латинских букв. Во второй строке число K (1 ≤ K ≤ 10).
#
# Выходные данные
#
# Требуется вывести результат расшифровки.
#
# Sample Input 1:
#
# XPSE
# 1
# Sample Output 1:
#
# WORD
# Sample Input 2:
#
# ZABC
# 3
# Sample Output 2:
#
# WXYZ

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k;

def get_newValue(v, k):
    newVal = v - k;
    if newVal >= 1:
        return newVal;
    else:
        return 26 + newVal;

string = input();
k = int(input());

alf = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'};

for i in range(len(string)):
    val = get_key(alf, string[i]);
    newVal = get_newValue(val, k);
    print(alf.get(newVal), end='');