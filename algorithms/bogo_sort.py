import random
from utils import get_random_numbers_list




numbers = get_random_numbers_list(10)


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    while not is_sorted(values):
        random.shuffle(values)
    return values


if __name__ == "__main__":
    print(bogo_sort(numbers))