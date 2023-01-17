# Сортировка слиянием
# Отсортируйте данный массив, используя сортировку слиянием.
#
# Входные данные
#
# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее идет N целых чисел, не превосходящих по абсолютной величине 109.
#
# Выходные данные
#
# Выведите эти числа в порядке неубывания.
#
# Sample Input:
#
# 2
# 3 1
# Sample Output:
#
# 1 3

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1
    return nums

n = int(input())
arr = list(map(int, input().split(" ")))
print(*merge_sort(arr))