# Дано N чисел, требуется выяснить, сколько среди них различных.
#
# Входные данные
#
# В первой строке дано число N – количество чисел. (1 <= N <= 100000) Во второй строке даны через пробел N чисел, каждое не превышает 2*109 по модулю.
#
# Выходные данные
#
# Выведите число, равное количеству различных чисел среди данных.
#
# Sample Input:
#
# 5
# 1 0 1 2 0
# Sample Output:
#
# 3

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array

n = int(input())
arr = list(map(int, input().split(" ")))
arr = sort(arr)

count=1

for i in range(1, len(arr)):
    if arr[i] - arr[i-1] != 0:
        count +=1

print(count)
