def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0
        n, m, o = len(L), len(R), len(arr)
        while k < o:
            if i < n and j < m and L[i] > R[j]:
                arr[k] = R[j]
                j += 1
            elif i < n and j < m and L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            elif i < n:
                arr[k] = L[i]
                i += 1
            elif j < m:
                arr[k] = R[j]
                j += 1
            k += 1


arr = [-1, 10, 5, 8, 9, 3, 6, 15, 12, 16, 69, 0, 24, 1]
mergeSort(arr)
print(arr)
