from utils import time_it


def linear_search(list, val):
    for index, element in enumerate(list):
        if element == val:
            return index
    return -1


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


def binary_search_recursive(list, val):
    pass


if __name__ == "__main__":
    list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 24
    index = linear_search(list, number_to_find)
    print(f"number found at index {index} using linear search ")

    index2 = binary_search(list, number_to_find)
    print(f"number found at index {index2} using binary search ")
