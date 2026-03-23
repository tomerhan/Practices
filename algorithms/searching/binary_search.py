"""
Binary Search
-------------
Efficiently finds a target value in a sorted list.
Time complexity: O(log n)  |  Space complexity: O(1) iterative, O(log n) recursive

Requirement: the input list must be sorted.
"""


def binary_search(arr, target):
    """Return the index of target in arr, or -1 if not found."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low=None, high=None):
    """Recursive variant. Return the index of target in arr, or -1 if not found."""
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    idx = binary_search(sorted_list, target)
    print(f"Iterative: found {target} at index {idx}")

    idx = binary_search_recursive(sorted_list, target)
    print(f"Recursive: found {target} at index {idx}")

    missing = binary_search(sorted_list, 6)
    print(f"Searching for 6 (not in list): index {missing}")
