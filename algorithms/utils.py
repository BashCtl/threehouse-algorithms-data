import random
import time
from faker import Faker
import quicksort

fake = Faker()


def get_random_numbers_list(amount):
    result = [x for x in range(1, amount + 1)]
    random.shuffle(result)
    random.shuffle(result)
    return result


def get_names(amount):
    names = [fake.name() for _ in range(amount)]
    random.shuffle(names)
    return names


def write_sorted_names(amount, filename):
    sorted = quicksort.quicksort(get_names(amount))
    print(sorted)
    with open(filename, "w") as file:
        for name in sorted:
            file.write(name)
            file.write("\n")



def performance(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        diff = end - start
        print(f"Time to execute: {diff:.6f} seconds")
        return result

    return wrapper


if __name__ == "__main__":
    write_sorted_names(10000, "sorted_names.txt")