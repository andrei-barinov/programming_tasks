# Шарики
# В одной компьютерной игре игрок выставляет в линию шарики разных цветов. Когда образуется непрерывная цепочка из трех и более шариков одного цвета, она удаляется из линии. Все шарики при этом сдвигаются друг к другу, и ситуация может повториться.
#
# Напишите программу, которая по данной ситуации определяет, сколько шариков будет "уничтожено". Естественно, непрерывных цепочек из трех и более одноцветных шаров в начальный момент может быть не более одной.
#
# Входные данные
#
# Сначала вводится количество шариков в цепочке (не более 1000) и цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число).
#
# Выходные данные
#
# Требуется вывести количество шариков, которое будет "уничтожено".
#
# Sample Input:
#
# 5 1 3 3 3 2
# Sample Output:
#
# 3

def makeCommonArr(arr):
    temp = 1;
    arrCommon = [];
    arrItem = [];

    arrItem.append(arr[0]);
    arrItem.append(0);
    arrItem.append(temp);
    arrCommon.append(arrItem);
    arrItem = [];

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            indexEndTmp = i;
            temp += 1;
            arrItem.append(arr[i]);
            arrItem.append(i);
            arrItem.append(temp);
            arrCommon.append(arrItem);
            arrItem = [];
        if arr[i] != arr[i - 1]:
            temp = 1;
            arrItem.append(arr[i]);
            arrItem.append(i);
            arrItem.append(temp);
            arrCommon.append(arrItem);
            arrItem = [];

    return arrCommon;


def findItemWithMaxTmp(arr):
    maxTemp = 0;

    for i in range(len(arrCommon)):
        if arrCommon[i][2] > maxTemp:
            maxTemp = arrCommon[i][2];
            item = arrCommon[i];
    return item;


def makeNewArr(arr, item):
    tmp = item[2];
    indexEnd = item[1];
    indexBegin = indexEnd - (tmp - 1);
    newArr = [];

    for i in range(len(arr)):
        if i < indexBegin or i > indexEnd:
            newArr.append(arr[i][0]);

    return newArr;


inArr = input().split(" ");

arr = [];

for i in range(1, len(inArr)):
    arr.append(inArr[i]);

s = 0;

while (True):
    arrCommon = makeCommonArr(arr);
    arrItemWithMaxTmp = findItemWithMaxTmp(arrCommon);
    arrMod = makeNewArr(arrCommon, arrItemWithMaxTmp);

    if arrItemWithMaxTmp[2] == len(arrCommon) and arrItemWithMaxTmp[2] >= 3:
        s += arrItemWithMaxTmp[2];
        break;
    if arrItemWithMaxTmp[2] >= 3:
        s += arrItemWithMaxTmp[2];
    else:
        break;
    arr = arrMod;

print(s);