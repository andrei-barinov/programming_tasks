# Идеальный отряд
# Как вы помните, месклиниты отправились в экспедицию. Однажды руководителю экспедиции потребовалось отправить на разведку специальный отряд, состоящих из лучших месклинитов. Для этого он выстроил всю команду в шеренгу.
#
# Цвет панциря каждого месклинита обозначается заглавной латинской буквой (от "A" до "Z" ). В целях экономии времени руководитель собирается выбрать из шеренги несколько подряд стоящих. Кроме того, он считает, что разведка будет более удачной, если выбранный отряд будет симметричен по цветам панцирей. Например, отряд "RGBGR" будет симметричным, а отряд "RGRB"  – нет.
#
# Требуется выбрать из шеренги месклинитов максимально возможный отряд, удовлетворяющий данным условиям.
#
# Входные данные
#
# Дана строка, длина которой не превосходит 255 символов – цвета месклинитов в шеренге.
#
# Выходные данные
#
# Выходные данные представляют собой строку – выбранный отряд месклинитов. Если возможных вариантов ответа несколько, то требуется вывести находящийся ближе к началу шеренги.
#
# Sample Input:
#
# ABAC
# Sample Output:
#
# ABA

def getResultFromReverseString(arrResult):
    newArrResult = [];
    for val in arrResult:
        compStr = val[::-1];
        if len(val) % 2 == 0:
            if val != compStr:
                continue;
            else:
                newArrResult.append(val);
        else:
            newArrResult.append(val);
    return newArrResult;


def checkArrResultOnSymmetry(arrResult):
    for val in arrResult:
        if len(val) % 2 == 1:
            sliceStr = val[:len(val) // 2];
            bool = True;
            for i in range(1, len(sliceStr)):
                if sliceStr[0] != sliceStr[i]:
                    bool == False;
                    break;
            if bool == False:
                continue;
            else:
                newArrResult.append(val);
        else:
            newArrResult.append(val);
    return newArrResult;


def getResult(newArrResult):
    max = newArrResult[0];
    for i in range(1, len(newArrResult)):
        if len(newArrResult[i]) > len(max):
            max = newArrResult[i];
    return max;


string = input();
a = 0;
b = len(string) - 1;
d = [];
arrResult = [];
while True:
    while a != b:
        litterOne = string[a];
        litterTwo = string[b];
        if litterOne == litterTwo:
            d.append(b);
            a += 1;
            b -= 1;
            if a > b // 2: break;
        else:
            d = [];
            a = 0;
            b -= 1;
            if a > b // 2: break;
    if len(string) > 2:
        if len(d) != 0:
            result = '';
            for i in range(max(d) + 1):
                result += string[i];
            arrResult.append(result);
        string = string = string[1:];
        a = 0;
        b = len(string) - 1;
        d = [];
    else:
        break;
newArrResult = [];

arrResult = getResultFromReverseString(arrResult);
newArrResult = checkArrResultOnSymmetry(arrResult);

print(getResult(newArrResult));