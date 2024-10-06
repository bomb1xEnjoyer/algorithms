from random import randint


def bubble_sort(lst):
    n =  len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


nums = [randint(1, 100) for _ in range(10)]
print(nums)
sorted_nums = bubble_sort(nums)
print(sorted_nums)
