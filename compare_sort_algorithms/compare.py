import sys
import os
import timeit
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sort_algorithms.insertion_sort.python.insertion_sort import insertion_sort
from sort_algorithms.merge_sort.python.merge_sort import merge_sort
from sort_algorithms.quick_sort.python.quick_sort import quick_sort

def generate_test_data(size, data_range):
    """Generate a list of random integers."""
    return [random.randint(*data_range) for _ in range(size)]

def compare_sort(test_data):
    results = {}

    # Insertion Sort
    start_time = timeit.default_timer()
    insertion_sort(test_data.copy())
    end_time = timeit.default_timer()
    results["Insertion Sort"] = end_time - start_time

    # Quick Sort
    start_time = timeit.default_timer()
    quick_sort(test_data.copy())
    end_time = timeit.default_timer()
    results["Quick Sort"] = end_time - start_time

    # Merge Sort
    start_time = timeit.default_timer()
    merge_sort(test_data.copy())
    end_time = timeit.default_timer()
    results["Merge Sort"] = end_time - start_time

    # Built-in Sorted
    start_time = timeit.default_timer()
    sorted(test_data.copy())
    end_time = timeit.default_timer()
    results["Built-in Sorted"] = end_time - start_time

    return results

def analyze_algorithms():
    test_sizes = [100, 1000, 10000]
    data_range = (1, 1000000)

    for size in test_sizes:
        print(f"\nTesting with array size: {size}")
        test_data = generate_test_data(size, data_range)
        results = compare_sort(test_data)

        for sort_method, execution_time in results.items():
            print(f"{sort_method}: {execution_time:.10f} seconds")

if __name__ == "__main__":
    analyze_algorithms()
