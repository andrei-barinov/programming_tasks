# Экспедиция
# Месклиниты собрались в экспедицию на край света. У них есть корабль, состоящий из N × M плотиков, связанных между собой. У каждого плотика есть своя грузоподъемность, а у каждого месклинита – своя масса. На каждом плотике может находиться не более одного месклинита. Если грузоподъемность выбранного плотика меньше массы месклинита, то бедный месклинит утонет при посадке.
#
# Руководитель экспедиции продумывает рассадку по плотикам. Помогите ему определить, какому максимальному количеству месклинитов удастся отправиться в путь.
#
# Входные данные
#
# В первой строке даны числа N и M (1 ≤ N, M ≤ 40). В каждой из последующих N строк содержится по M чисел, обозначающих грузоподъемность соответствующего плотика. В (N+2)-ой строке находится число K (1 ≤ K ≤ 2000) – количество месклинитов. В (N+3)-ей строке содержатся K чисел, i-ое из которых – масса i-ого месклинита. Все массы месклинитов и грузоподъемности плотиков – натуральные числа, не превышающие 109.
#
# Выходные данные
#
# Требуется вывести одно число – максимально возможное количество участников экспедиции.
#
# Sample Input:
#
# 3 2
# 5 10
# 7 5
# 5 5
# 6
# 9 5 3 5 12 10
# Sample Output:
#
# 4

def sort_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


n, m = map(int, input().split(" "))

arr = []
for i in range(n):
    arr1 = list(map(int, input().split(" ")))
    for j in range(m):
        arr.append(arr1[j])

k = int(input())
arr2 = list(map(int, input().split(" ")))

arr = sort_arr(arr)
arr2 = sort_arr(arr2)

count = 0

if n * m >= k:
    for i in range(len(arr2)):
        for j in range(len(arr)):
            if arr2[i] <= arr[j]:
                arr.pop(j)
                count += 1
                break
else:
    for i in range(len(arr)):
        for j in range(len(arr2)):
            if arr2[j] <= arr[i]:
                arr2.pop(j)
                count += 1
                break

print(count)