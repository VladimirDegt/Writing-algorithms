def merge_sort(list):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    Merge sort is a divide-and-conquer algorithm that splits the list into 
    smaller sublists, recursively sorts each sublist, and then merges the 
    sorted sublists to produce the final sorted list.
    Args:
        list (List): The list of elements to be sorted.
    Returns:
        List: A new list containing all elements from the input list in 
        ascending order.
    """
    if len(list) <= 1:
        return list;
    mid = len(list) // 2
    left_part = list[:mid];
    right_part = list[mid:];

    return merge(merge_sort(left_part), merge_sort(right_part))

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
    Returns:
        list: A merged and sorted list containing all elements from both input lists.
    """
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

not_sort_array = [5, 3, 8, 4, 2]

print('not_sort_array-->', not_sort_array)
print('sort_array-->', merge_sort(not_sort_array))