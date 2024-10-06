from random import randint


def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        current = lst[i]
        j = i
        while j > 0 and lst[j - 1] > current:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = current


nums = [randint(1, 100) for _ in range(10)]
print(nums)
insertion_sort(nums)
print(nums)
