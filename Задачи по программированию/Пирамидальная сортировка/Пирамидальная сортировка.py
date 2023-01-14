# Пирамидальная сортировка
# Отсортируйте данный массив. Используйте пирамидальную сортировку.
#
# Входные данные
#
# Первая строка входных данных содержит количество элементов в массиве N,  N  ≤  105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.
#
# Выходные данные
#
# Выведите эти числа в порядке неубывания.
#
# Sample Input:
#
# 5
# 5 4 3 2 1
# Sample Output:
#
# 1 2 3 4 5

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums


n = int(input())
arr = list(map(int, input().split(" ")))
print(*heap_sort(arr))