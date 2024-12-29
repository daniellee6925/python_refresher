"""
divide and conquer
compare elements based on pivot value
Partition: putting pivot in the right position
start pointer: stop when value greater than pivot
end pointer: stop when value less than pivot
when end pointer comes before start pointer, swap end pointer with pivot
"""


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]
    """
    if a != b
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    """


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] >= pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(end, pivot_index, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index - 1)  # left partition
        quick_sort(elements, partition_index + 1, end)  # right partition


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
