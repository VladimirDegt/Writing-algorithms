def selection_sort(list):
    """
    Sorts a list of elements in ascending order using the selection sort algorithm.
    Parameters:
    list (list): The list of elements to be sorted.
    Returns:
    list: The sorted list in ascending order.
    """
    n = len(list);
    for i in range(n):
        min_idx = i;
        for j in range(i + 1, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i];
    
    return list;

not_sort_array = [5, 3, 8, 4, 2];

print('not_sort_array-->', not_sort_array)
print('sort_array-->', selection_sort(not_sort_array))