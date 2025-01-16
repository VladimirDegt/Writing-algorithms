def compute_lps(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for a given pattern.

    Parameters:
    pattern (str): The pattern for which to compute the LPS array.

    Returns:
    list: The LPS array.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    """
    Perform the Knuth-Morris-Pratt (KMP) search algorithm to find the first occurrence of a pattern in a main string.

    Parameters:
    main_string (str): The main string in which to search for the pattern.
    pattern (str): The pattern to search for.

    Returns:
    int: The starting index of the first occurrence of the pattern in the main string, or -1 if the pattern is not found.
    """
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1

raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."

pattern = "алг"

print(kmp_search(raw, pattern))
