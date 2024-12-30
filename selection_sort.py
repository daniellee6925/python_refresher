"""
time complexity O(n^2)
find minimum element from unsorted portion of the array
"""


def find_min_element(arr):
    min_element = 100000
    for i in range(len(arr)):
        if arr[i] < min:
            min_element = arr[i]
    return min_element


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(min_index, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def selection_sort_by_name(arr, key_pref_list):
    for key_pref in key_pref_list[::-1]:  # reverses array
        for i in range(len(arr)):
            min_index = i
            for j in range(min_index, len(arr)):
                if arr[j][key_pref] < arr[min_index][key_pref]:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    elements = [78, 12, 15, 8, 61, 53, 32, 27]
    names = [
        {"First Name": "Raj", "Last Name": "Nayyar"},
        {"First Name": "Suraj", "Last Name": "Sharma"},
        {"First Name": "Karan", "Last Name": "Kumar"},
        {"First Name": "Jade", "Last Name": "Canary"},
        {"First Name": "Raj", "Last Name": "Thakur"},
        {"First Name": "Raj", "Last Name": "Sharma"},
        {"First Name": "Kiran", "Last Name": "Kamla"},
        {"First Name": "Armaan", "Last Name": "Kumar"},
        {"First Name": "Jaya", "Last Name": "Sharma"},
        {"First Name": "Ingrid", "Last Name": "Galore"},
        {"First Name": "Jaya", "Last Name": "Seth"},
        {"First Name": "Armaan", "Last Name": "Dadra"},
        {"First Name": "Ingrid", "Last Name": "Maverick"},
        {"First Name": "Aahana", "Last Name": "Arora"},
    ]
    sort_by = ["First Name", "Last Name"]
    selection_sort(elements)
    selection_sort_by_name(names, sort_by)
    print(names)
