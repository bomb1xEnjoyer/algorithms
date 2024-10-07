from random import randint


def merge(lst, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = lst[left + i]
    for j in range(n2):
        R[j] = lst[middle + 1 + j]
    k = left
    i, j = 0, 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        lst[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        lst[k] = R[j]
        j += 1
        k += 1


def merge_sort(lst, left, right):
    if left < right:
        middle = left + (right - left) // 2
        merge_sort(lst, left, middle)
        merge_sort(lst, middle + 1, right)
        merge(lst, left, middle, right)


nums = [randint(1, 100) for _ in range(10)]
print(nums)
merge_sort(nums, 0, 9)
print(nums)


