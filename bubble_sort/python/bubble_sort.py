def bubble_sort(input_list):
    """
    Sorts a list of elements in ascending order using the bubble sort algorithm.

    This algorithm works by repeatedly swapping adjacent elements if they are in the wrong order.

    Args:
        input_list (list): The list of elements to be sorted.

    Returns:
        list: A sorted list of elements in ascending order.
    """
    n = len(input_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            print('the state of the array-->', input_list)
    return input_list

not_sort_array = [5, 3, 8, 4, 2]

print('not_sort_array-->', not_sort_array)
print('sort_array-->', bubble_sort(not_sort_array))
