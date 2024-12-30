"""
time complexity O(nlogn)
divide and conquer
continuosly divde the array into half until only single elements are left
merge the elements in order for each level
"""


def merge_sort(arr):
    # exit conditions
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    # split the array into two
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
    while i < len_a and j < len_b:
        if (
            a[i] < b[j]
        ):  # insert element from left list. don't touch element from right list
            arr[k] = a[i]
            i += 1  # move pointer for left list by 1
        else:
            arr[k] = b[j]
            j += 1  # move pointer for right list by 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1  # move pointer for left list by 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1  # move pointer for left list by 1
        k += 1


def merge_sort_by_time(elements, key="time_hours", descending=True):
    if len(elements) <= 1:
        return
    mid = len(elements) // 2
    # split the array into two
    left = elements[:mid]
    right = elements[mid:]

    merge_sort_by_time(left, key, descending)
    merge_sort_by_time(right, key, descending)
    merge_two_sorted_lists_by_time(left, right, arr, key, descending)


def merge_two_sorted_lists_by_time(a, b, arr, key, descending):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
    while i < len_a and j < len_b:
        if (
            a[i][key] < b[j][key]
        ):  # insert element from left list. don't touch element from right list
            arr[k] = a[i]
            i += 1  # move pointer for left list by 1
        else:
            arr[k] = b[j]
            j += 1  # move pointer for right list by 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1  # move pointer for left list by 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1  # move pointer for left list by 1
        k += 1


if __name__ == "__main__":
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]
    arr = [5, 8, 12, 56, 7, 9, 45, 51]
    merge_sort(arr)

    print(arr)

    elements = [
        {"name": "vedanth", "age": 17, "time_hours": 1},
        {"name": "rajab", "age": 12, "time_hours": 3},
        {"name": "vignesh", "age": 21, "time_hours": 2.5},
        {"name": "chinmay", "age": 24, "time_hours": 1.5},
    ]

    merge_sort_by_time(elements)
    print(elements)
