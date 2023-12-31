def binary_search(lst, target):
    first = 0
    last = len(lst) - 1
    while first <= last:
        midpoint = (first + last) // 2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found at list.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 2)
verify(result)

result = binary_search(numbers, 7)
verify(result)