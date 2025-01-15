def binary_search(arr, target):
    """
    Perform a binary search on a sorted array to find the index of a target value.

    Parameters:
    arr (list): A sorted list of elements to search.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")