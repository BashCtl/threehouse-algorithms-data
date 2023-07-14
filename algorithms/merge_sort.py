import random


def merge_sort(lst):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublist created in previous step

    Takes O(n log n) times
    """
    if len(lst) <= 1:
        return lst
    left_half, right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def split(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(log n) time
    """
    midpoint = len(lst) // 2
    return lst[:midpoint], lst[midpoint:]


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    Runs in overall O(n) time
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1

    return l


numbers = [x for x in range(100)]
random.shuffle(numbers)
random.shuffle(numbers)
print(numbers)


def verify_sorted(lst):
    n = len(lst)
    if n == 0 or n == 1:
        return True
    return lst[0] < lst[1] and verify_sorted(lst[1:])


print(verify_sorted(numbers))
numbers = merge_sort(numbers)
print(verify_sorted(numbers))
