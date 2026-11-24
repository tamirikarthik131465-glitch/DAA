
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        # Restore Max-Heap
        heapify(arr, i, 0)

    return arr


# Example
arr = [12, 11, 13, 5, 6, 7]

print("Original Array:", arr)
heap_sort(arr)
print("Sorted Array:", arr)
