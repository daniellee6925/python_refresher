from util import time_it


@time_it
def linear_search(list, val):
    for index, element in enumerate(list):
        if element == val:
            return index
    return -1


@time_it
def binary_search(list, val):
    left_index = 0
    right_index = len(list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2  # returns int for index with //
        mid_number = list[mid_index]

        if mid_number == val:
            return mid_index
        elif mid_number < val:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(list, val, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2  # returns int for index with //

    if mid_index >= len(list) or mid_index < 0:
        return -1

    mid_number = list[mid_index]

    if mid_number == val:
        return mid_index

    elif mid_number < val:
        return binary_search_recursive(list, val, mid_index + 1, right_index)

    else:
        return binary_search_recursive(list, val, left_index, mid_index - 1)


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == "__main__":
    list = [12, 15, 17, 19, 21, 24, 45, 67]
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    # list = [i for i in range(1000000)]
    # number_to_find = 1000000

    index = linear_search(list, number_to_find)
    print(f"number found at index {index} using linear search ")

    index2 = binary_search_recursive(list, number_to_find, 0, len(list) - 1)
    print(f"number found at index {index2} using binary search ")

    arr = find_all_occurances(numbers, number_to_find)
    print(f"number found at index {arr} using binary search ")
