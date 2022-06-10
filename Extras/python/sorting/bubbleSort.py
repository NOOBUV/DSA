def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        temp = 0
        for j in range(i+1, n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                temp += 1
        if temp == n-i-1:
            break
    print(arr)


bubbleSort([1, 2, 3, 4, 5])
