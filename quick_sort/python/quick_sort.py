def quick_sort(arr):
    """
    Sorts a list of elements using the quick sort algorithm.
    Args:
        arr (List): The list of elements to be sorted.
    Returns:
        List: A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left_part = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right_part = [x for x in arr if x > pivot]
    return quick_sort(left_part) + middle + quick_sort(right_part)

not_sort_array = [5, 3, 8, 4, 2]

print('not_sort_array-->', not_sort_array)
print('sort_array-->', quick_sort(not_sort_array))