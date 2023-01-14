# Учащиеся без троек
# Выведите фамилии и имена учащихся, не имеющих троек (а также двоек и колов).
#
# Входные данные
#
# Заданы сначала количество учащихся n, затем n строк, каждая из которых содержит фамилию, имя и три числа (оценки по трем предметам: математике, физике, информатике). Данные в строке разделены одним пробелом. Оценки принимают значение от 1 до 5.
#
# Выходные данные
#
# Необходимо вывести пары фамилия-имя по одной на строке, разделяя фамилию и имя одним пробелом. Выводить оценки не нужно. Порядок вывода должен быть таким же, как в исходных данных.
#
# Sample Input 1:
#
# 3
# Babat Anna 5 4 3
# Belova Galina 4 3 5
# Moroz Yaroslav 3 5 4
# Sample Output 1:
#
# Sample Input 2:
#
# 2
# Krasnov Ivan 5 5 5
# Shusha Andrey 1 2 4
# Sample Output 2:
#
# Krasnov Ivan

def checkMark(a, b, c):
    return a > 3 and b > 3 and c > 3;

n = int(input());
arr = [];
arr1 = [];

for i in range(n):
    st=input().split(" ");
    if checkMark(int(st[2]), int(st[3]), int(st[4])):
        st = st[0] + " " + st[1];
        arr.append(st);
if len(arr) != 0:
    for val in arr:
        print(val);
else:
    print();