# Поиск подстроки
# Даны две строки. Определите, является ли первая строка подстрокой второй строки.
#
# Входные данные
#
# На вход подается 2 строки длины не более 10000, состоящие только из маленьких букв латинского алфавита.
#
# Выходные данные
#
# Необходимо вывести  слово yes, если первая строка является подстрокой второй строки, или слово no в противном случае.
#
# Sample Input:
#
# abac
# ababacaba
# Sample Output:
#
# yes

string1 = input();
string2 = input();

if len(string1) > len(string2):
    maxStr = string1;
    minStr = string2;
else:
    maxStr = string2;
    minStr = string1;

arr=[];

a = 0;
b = len(minStr);

for j in range(len(maxStr) - len(minStr) + 1):
    for i in range(a, b):
        arr.append(maxStr[i]);
    newStr = ''.join(arr);
    arr=[];
    if newStr == minStr:
        print('yes');
        break;
    if j == len(maxStr) - len(minStr):
        print('no');
    a +=1;
    b +=1;