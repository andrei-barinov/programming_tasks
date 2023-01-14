# Хипуй!
# В этой задаче вам необходимо организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции:
#
#    a) Insert(k) – добавить в Heap число k (1 ≤  k ≤ 1000000) ;
#    b) Extract достать из Heap наибольшее число (удалив его при этом).
#
# Входные данные
#
# В первой строке содержится количество команд N (1 ≤  N ≤ 100000), далее следуют N команд, каждая в своей строке.  Команда может иметь  формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполенении команды Extract в структуре находится по крайней мере один элемент.
#
# Выходные данные
#
# Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.
#
# Sample Input:
#
# 2
# 0 10000
# 1
# Sample Output:
#
# 10000

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(num)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


def heap_sort(nums):
    size = len(nums)
    for i in range(size, -1, -1):
        heapify(nums, size, i)

    for i in range(size - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums


n = int(input())
arrForHeap = []

for i in range(n):
    arr = list(map(int, input().split(" ")))

    if arr[0] == 0:
        m = arr[1]
        insert(arrForHeap, m)
    if arr[0] == 1:
        print(heap_sort(arrForHeap)[len(arrForHeap) - 1])
        deleteNode(arrForHeap, arrForHeap[len(arrForHeap) - 1])