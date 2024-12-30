"""
move pointer through the arry.
Compare the current element to the previous elments (from index - 1 to 0)
insert elmenet where greater than left and less than right
time complexitiy
worst, average O(n^2)
best O(n)
space complexity
O(n)
"""


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor


def print_median(elements):
    for i in range(1, len(elements) + 1):
        curr = elements[:i]
        insertion_sort(curr)

        size = len(curr)

        if size == 1:
            print(curr[0])
            continue

        median_index = (size - 1) // 2
        # list has even numbers
        if size % 2 == 0:
            median_value = (curr[median_index] + curr[median_index + 1]) / 2
        else:
            median_value = curr[median_index]
        print(median_value)


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    sequence = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
    print_median(sequence)
    print(elements)
