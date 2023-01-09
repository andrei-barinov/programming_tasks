# Первоклассная задача
# Преподаватель по программированию некоего Центра для одаренных детей, узнав, что его ученики знают математику 3-го класса на 97.001 процентов, решил проверить их знания по курсу математики 1-го класса. Для этого он взял за основу популярнейшую у математиков 1-го класса задачу. Первоклассник должен был продолжить следующую последовательность рядов:
#
# 1
#
# 11
#
# 21
#
# 1211
#
# 111221
#
# 312211
#
# 13112221
#
# Входные данные
#
# В единственной строке входного файла записаны два целых числа через пробел: x (0 <= x <= 100) - первый член последовательности и n (1 <= n <= 25).
#
# Выходные данные
#
# Выведите n-ый ряд x-ой последовательности.
#
# Sample Input:
#
# 1 4
# Sample Output:
#
# 1211

x, n = input().split(' ');

def getResult(string):
    arrResult = [[1, string[0]]];
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            arrResult[len(arrResult) - 1][0] = arrResult[len(arrResult) - 1][0] + 1;
        else:
            arrResult.append([1, string[i]]);
    strResult = '';
    for i in range(len(arrResult)):
        strResult += str(arrResult[i][0]) + arrResult[i][1];
    return strResult;

string = x;

if int(n) == 1:
    print(string);
else:
    for i in range(1, int(n)):
        if n == 2:
            result = string + '1';
        else:
            result = getResult(string);
            string = result;
    print(result);