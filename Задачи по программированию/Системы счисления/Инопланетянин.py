# Инопланетянин
# Во время эксперимента Накодиллы было случайно получено сообщение инопланетян, содержащее формулу вида A + B = C.
#
# Общественности стало интересно, какую же систему счисления используют инопланетяне. Так как внеземная цивилизация была достаточно развита, чтобы отправить межпланетное сообщение, Накодилла предположил, что основание системы счисления довольно мало. Требуется написать программу, которая находит минимальное основание системы счисления, при котором данное равенство выполняется.
#
# Входные данные
#
# В единственной строке входных данных содержится равенство вида A + B = C. Строка не содержит пробелы, числа состоят из цифр от 0 до 9 и заглавных латинских букв от А до Z
#
# Выходные данные
#
# Требуется вывести единственное число – искомое основание системы счисления. Если такой системы счисления не существует, то вывести -1. Гарантируется, что ответ не превышает 36.
#
# Sample Input:
#
# 2+2=4
# Sample Output:
#
# 5

def convertToK(k, A):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
           22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
           34: 'Y', 35: 'Z'}

    arr = []

    while True:
        d = A % k
        if d > 9:
            arr.append(dic[d])
        else:
            arr.append(str(d))
        A = A // k
        if A == 0:
            break

    arr.reverse()
    res = [str(x) for x in arr]

    return ''.join(res)


arrIn = input().split("=")
arrIn2 = arrIn[0].split("+")

a = arrIn2[0]
b = arrIn2[1]
c = arrIn[1]

arr = []
arr1 = []

for k in range(2, 37):
    for j in range(10000):
        f = convertToK(k, j)
        arr1.append(k)
        arr1.append(j)
        arr1.append(f)
        arr.append(arr1)
        arr1 = []

arrA = []
arrB = []
arrC = []

for i in range(len(arr)):
    if arr[i][2] == a:
        arrA.append(arr[i])
    if arr[i][2] == b:
        arrB.append(arr[i])
    if arr[i][2] == c:
        arrC.append(arr[i])

n = -1
flag = True
for i in range(len(arrA)):
    if flag == False:
        break
    for j in range(len(arrB)):
        if flag == False:
            break
        for k in range(len(arrC)):
            l = arrA[i][1] + arrB[j][1]
            if l == arrC[k][1] and arrA[i][0] == arrB[j][0] and arrB[j][0] == arrC[k][0]:
                n = arrA[i][0]
                flag = False
                break

print(n)