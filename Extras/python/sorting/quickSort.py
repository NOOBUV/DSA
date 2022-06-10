def partition(arr, l, r):
    pivot = arr[l]
    i = l + 1
    j = r
    while i < j:
        while i < r and arr[i] <= pivot:
            i += 1
        while j > l and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # if arr[j] < pivot:
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quickSort(arr, l, r):
    if l >= r:
        return
    part = partition(arr, l, r)
    quickSort(arr, l, part-1)
    quickSort(arr, part+1, r)


arr = [-1, 10, 5, 8, 9, 3, 6, 15, 12, 16, 69, 0, 24, 1, 5]
quickSort(arr, 0, 14)
print(arr)
