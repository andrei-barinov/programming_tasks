# Интересный перевод
# На планете Роботов очень не любят десятичную систему счисления, поэтому они попросили Вас написать программу, которая заменяет все встречающиеся в тексте числа на эти же числа, но в двоичной системе счисления.
#
# Входные данные
#
# Единственная строка, состоящая из любых символов. Длина строки не превышает 255 символов. Гарантируется, что во всех числах нет ведущих нулей.
#
# Выходные данные
#
# Выведите преобразованную строку.
#
# Sample Input:
#
# 6^&678JKjdkdl;?.,lk879Pk1kdfl4839
# Sample Output:
#
# 110^&1010100110JKjdkdl;?.,lk1101101111Pk1kdfl1001011100111

string = input();

def getDigitArr(string):
    arrDigit = [];
    newArrDigit = [];
    for i in range(len(string)):
        if i == 0:
            if string[i].isdigit():
                arrDigit.append(string[i]);
                continue;
        if string[i].isdigit() and string[i-1].isdigit():
            arrDigit[len(arrDigit)-1] += string[i];
            continue;
        if string[i].isdigit():
            arrDigit.append(string[i]);
    for j in range(len(arrDigit)):
        newArrDigit.append([arrDigit[j], getDoubleDigit(int(arrDigit[j]))]);
    return newArrDigit;

def getDoubleDigit(digit):
    arrDouble = [];
    stringDouble = '';
    if int(digit) == 1 or int(digit) == 0:
        return str(digit);
    else:
        while digit >= 2:
            result = digit % 2;
            arrDouble.append(result);
            digit //= 2;
            if digit == 0 or digit == 1:
                arrDouble.append(digit);
    for i in range(len(arrDouble)-1, -1, -1):
        stringDouble += str(arrDouble[i]);
    return stringDouble;

digitArr = getDigitArr(string);
newString ='';
smallStr = '';

while True:
    for i in range(len(string)):
        if string[i].isdigit():
            smallStr += string[i];
            if smallStr == digitArr[0][0]:
                newString += digitArr[0][1];
                digitArr.pop(0);
                string = string.replace(smallStr, "", 1);
                smallStr = '';
                break;
        else:
            newString += string[i];
            string = string.replace(string[i], "", 1);
            break;
    if len(string) == 0:
        break;
print(newString);