# Утренняя пробежка - 1
# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 70% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
#
# Входные данные
#
# На вход программа получает два действительных числа x и y . Числа положительные, действительные, не превосходят 1000, заданы с точностью до шести знаков после запятой.
#
# Выходные данные
#
# Программа должна вывести единственное целое число.
#
# Sample Input:
#
# 10 30
# Sample Output:
#
# 4

arr = input().split(" ");
x = float(arr[0]);
y = float(arr[1]);
i = 1;

while(True):
    if x >= y:
        print(i);
        break;
    else:
        x += 0.7*int(x*1e6)/1e6;
        i +=1;