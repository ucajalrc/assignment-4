import random

def randomized_quicksort(arr):
    """
    Sorts the array in-place using Randomized Quicksort.
    This algorithm works by choosing a random pivot for each partition,
    which avoids bad performance on already sorted or reverse-sorted arrays.
    """

    def quicksort_helper(array, low, high):
        if low < high:
            # Pick a random pivot index between low and high (inclusive)
            pivot_index = random.randint(low, high)
            # Swap the random pivot with the element at 'high' so partition works as usual
            array[pivot_index], array[high] = array[high], array[pivot_index]
            # Partition the array and get the position of the pivot after partitioning
            p = partition(array, low, high)
            # Recursively sort elements before and after partition
            quicksort_helper(array, low, p - 1)
            quicksort_helper(array, p + 1, high)

    def partition(array, low, high):
        """
        Lomuto partition scheme.
        Puts elements <= pivot on the left, > pivot on the right.
        Returns the index of the pivot in the partitioned array.
        """
        pivot = array[high]  # Pivot is now at the end
        i = low - 1  # Place for swapping
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        # Place pivot in correct spot
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    # Edge case: array is empty or only one element
    if arr is None or len(arr) <= 1:
        return arr
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr
