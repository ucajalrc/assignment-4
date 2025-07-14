def heapsort(arr):
    """
    Sorts an array in-place using the Heapsort algorithm.
    The function first builds a max-heap and then repeatedly extracts the maximum element,
    placing it at the end of the array, resulting in a sorted array in ascending order.
    """

    def heapify(arr, n, i):
        """
        Helper function to maintain the max-heap property for a subtree rooted at index i.
        If the parent node at index i violates the max-heap property,
        heapify will recursively swap it with its largest child until the property is restored.
        """
        largest = i              # Assume the root is the largest
        left = 2 * i + 1         # Index of the left child
        right = 2 * i + 2        # Index of the right child

        # Check if left child exists and is greater than the root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than the current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest value is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap parent with largest child
            heapify(arr, n, largest)                     # Recursively heapify the affected subtree

    n = len(arr)

    # Step 1: Build a max-heap from the array (bottom-up approach)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract the maximum element one by one and move it to the end of the array
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current max to the end
        heapify(arr, i, 0)               # Restore max-heap property in the reduced heap
