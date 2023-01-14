# Средний балл по предметам
# Определите средний балл всех учащихся по каждому предмету.
#
# Входные данные
#
# Заданы сначала количество учащихся n, затем n строк, каждая из которых содержит фамилию, имя и три числа (оценки по трем предметам: математике, физике, информатике). Данные в строке разделены одним пробелом. Оценки принимают значение от 1 до 5.
#
# Выходные данные
#
# Выведите три действительных числа (до 15  значащих цифр после запятой): средний балл всех учащихся по математике, по физике, по информатике.
#
# Sample Input:
#
# 2
# Markov Valeriy 4 5 2
# Kozlov Georgiy 5 1 2
# Sample Output:
#
# 4.5 3.0 2.0

n = int(input());
arr1 = [];
arr2 = [];
arr3 = [];

for i in range(n):
    st = input().split(" ");
    arr1.append(int(st[2]));
    arr2.append(int(st[3]));
    arr3.append(int(st[4]));

math = sum(arr1) / len(arr1);
phys = sum(arr2) / len(arr2);
inf = sum(arr3) / len(arr3)

print(math, phys, inf, sep=" ");