# Шеренга
# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
#
# Входные данные
#
# Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого с новой строки вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
#
# Выходные данные
#
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
#
# Sample Input 1:
#
# 165 163 160 160 157 157 155 154
# 162
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 165 163 160 160 157 157 155 154
# 160
# Sample Output 2:
#
# 5

arr = input().split(" ");
h = int(input());
b = 0;
s = True;

for i in range(len(arr)):
    if int(arr[i]) < h:
        b = i + 1;
        s = False;
        break;

if s and h == int(arr[len(arr) - 1]):
    b = len(arr) + 1;

print(b);