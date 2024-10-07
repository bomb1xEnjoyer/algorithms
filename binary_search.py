from random import randint


def first_bad_version(lst, left, right):
    while left <= right:
        middle = left + (right - left) // 2
        if lst[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return left



# Find first bad version
versions = [True for _ in range(randint(5, 20))] + [False for _ in range(randint(5, 20))]

print(versions)
print(versions.index(False) == first_bad_version(versions, 0, len(versions)))

print('-' * 20)


def binary_search(lst, left, right, target):
    while left <= right:
        middle = left + (right - left) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


nums = [randint(1, 100) for _ in range(1024)]
nums.sort()

print(binary_search(nums, 0, 1023, 50))
print(binary_search(sorted(nums), 0, 1023, 101))