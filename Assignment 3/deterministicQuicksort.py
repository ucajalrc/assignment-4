def deterministic_quicksort(arr):
    """
    Sorts the array in-place using Deterministic Quicksort.
    Always picks the first element as pivot. For sorted input, this leads to O(n^2) time and O(n) recursion depth,
    which can exceed Python's recursion limit for large arrays.
    """
    def quicksort_helper(array, low, high):
        if low < high:
            # Partition the array and get the pivot index
            p = partition(array, low, high)
            quicksort_helper(array, low, p - 1)    # Sort the left part
            quicksort_helper(array, p + 1, high)   # Sort the right part

    def partition(array, low, high):
        """
        Partition using first element as pivot.
        """
        pivot = array[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[low], array[i - 1] = array[i - 1], array[low]
        return i - 1

    if arr is None or len(arr) <= 1:
        return arr
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr
