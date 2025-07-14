import time
import random
import copy

def heapsort(arr):
    # (Insert the same heapsort code from above)
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def quicksort(arr):
    """
    Quicksort picks a pivot element and partitions the array into
    values less than and greater than the pivot, then recursively sorts.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right sides, then combine with pivot(s)
    return quicksort(left) + middle + quicksort(right)


def merge_sort(arr):
    """
    Merge Sort recursively divides the array into halves,
    sorts each half, and merges the sorted halves.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.
    """
    merged = []
    left_index, right_index = 0, 0

    # Compare elements and add the smaller one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def benchmark(sort_fn, arr):
    # Runs the sorting function on a copy of the array and measures elapsed time.
    arr_copy = copy.deepcopy(arr)
    start = time.perf_counter()
    if sort_fn == heapsort:
        sort_fn(arr_copy)
    else:
        arr_copy = sort_fn(arr_copy)
    return time.perf_counter() - start

for n in [1000, 10000]:
    print(f"\nArray size: {n}")
    for dtype in ['random', 'sorted', 'reverse']:
        if dtype == 'random':
            base = [random.randint(0, n) for _ in range(n)]
        elif dtype == 'sorted':
            base = list(range(n))
        else:
            base = list(range(n, 0, -1))
        t_heap = benchmark(heapsort, base)
        t_merge = benchmark(merge_sort, base)
        t_quick = benchmark(quicksort, base)
        print(f"{dtype:8} | Heap: {t_heap:.5f}s | Merge: {t_merge:.5f}s | Quick: {t_quick:.5f}s")
