def insertion_sort(arr):
    """
    Sorts an array of elements in ascending order using the insertion sort algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list of elements.
    """
    for i in range(1, len(arr)):
        current_element = arr[i];
        j = i - 1;
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j];
            j -= 1;
        arr[j + 1] = current_element;
    return arr

list_numbers = [5, 3, 8, 4, 2];

print(insertion_sort(list_numbers))