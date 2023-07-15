def index_of_item(collection, target):
    for index in range(0, len(collection)):
        if collection[index] == target:
            return index
    return None


