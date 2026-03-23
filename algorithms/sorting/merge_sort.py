"""
Merge Sort
----------
A divide-and-conquer sorting algorithm with O(n log n) time complexity.

Algorithm:
1. Divide the unsorted list into n sublists, each containing one element.
2. Repeatedly merge sublists to produce new sorted sublists until there is only one.
"""


def merge_sort(arr):
    """Sort a list using merge sort and return the sorted list."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {sample}")
    sorted_list = merge_sort(sample)
    print(f"Sorted:   {sorted_list}")
