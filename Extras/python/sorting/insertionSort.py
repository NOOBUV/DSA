arr = [12, 11, 13, 5, 6]


def insertSort(arr, dec):
    a, b = 0, 1
    while b < len(arr):
        i, j = a, b
        if not dec:
            while i >= 0 and arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i-1, j-1
        else:
            while i >= 0 and arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i-1, j-1
        a, b = a+1, b+1
    print(arr)


insertSort(arr, False)
