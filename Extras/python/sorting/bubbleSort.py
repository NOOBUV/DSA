def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    print(arr)


bubbleSort([5, 1, 4, 2, 8])
