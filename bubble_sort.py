"""
bubble sort
compare current and next.
if out of order, swap the two elements
time complexity O(n^2)
space complexity O(1)
"""


def bubble_sort(elements, key):
    size = len(elements)

    for k in range(size - 1):
        swapped = False
        for i in range(size - 1):
            if elements[i][key] > elements[i + 1][key]:
                # swap the 2 elements
                temp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
    ]

    bubble_sort(elements, "transaction_amount")
    print(elements)
