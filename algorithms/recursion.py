from utils import get_random_numbers_list
from utils import performance


@performance
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


@performance
def recursion_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursion_sum(numbers[1:])


if __name__ == "__main__":
    print(sum(get_random_numbers_list(100)))
    print(recursion_sum(get_random_numbers_list(100)))
