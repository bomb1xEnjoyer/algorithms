from random import randint


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot_index = randint(0, len(lst) - 1)
    pivot = lst[pivot_index]
    lower, equal, greater = [], [], []
    for item in lst:
        if item < pivot:
            lower.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)
    lower = quick_sort(lower)
    greater = quick_sort(greater)
    return lower + equal + greater


nums = [randint(1, 100) for _ in range(10)]
print(nums)
nums = quick_sort(nums)
print(nums)


