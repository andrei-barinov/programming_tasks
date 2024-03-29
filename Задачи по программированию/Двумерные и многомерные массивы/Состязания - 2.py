# Состязания - 2
# В метании молота состязается n спортсменов. Каждый из них сделал mбросков. Победителем соревнований объявляется тот спортсмен, у которого максимален наилучший результат по всем броскам. Таким образом, программа должна найти значение максимального элемента в данном массиве, а также его индексы (то есть номер спортсмена и номер попытки).
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа выводит значение максимального элемента, затем номер строки и номер столбца, в котором он встречается. Если в массиве несколько максимальных элементов, то нужно вывести минимальный номер строки, в которой встречается такой элемент, а если в этой строке таких элементов несколько, то нужно вывести минимальный номер столбца. Не забудьте, что все строки и столбцы нумеруются с 0.
#
# Sample Input:
#
# 3 3
# 3 1 2
# 1 3 4
# 3 3 3
# Sample Output:
#
# 4
# 1 2

arrIn = input().split(" ")
n = int(arrIn[0])
m = int(arrIn[1])

arr = []
maxEl = 0
nStr = 0
nColl = 0

for i in range(n):
    arr.append(input().split(" "))

for i in range(n):
    for j in range(m):
        if int(arr[i][j]) > int(maxEl):
            maxEl = arr[i][j]
            nColl = j
            nStr = i

print(maxEl)
print(nStr, nColl, sep=" ")