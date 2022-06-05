# def merge(arr, l, mid, r):
#     temp = [0 for i in range(r-l+1)]
#     i, j, k = l, mid+1, 0
#     while i <= mid and j <= r:
#         if arr[i] <= arr[j]:
#             temp[k] = arr[i]
#             k += 1
#             i += 1
#         else:
#             temp[k] = arr[j]
#             k += 1
#             j += 1
#     while i <= mid:
#         temp[k] = arr[i]
#         k += 1
#         i += 1
#     while j <= r:
#         temp[k] = arr[j]
#         k += 1
#         j += 1
#     k = 0
#     i = l
#     while i <= r:
#         arr[i] = temp[k]
#         i += 1
#         k += 1


# def mergeSort(arr, l, r):
#     if l < r:
#         mid = l + (r-l)//2
#         mergeSort(arr, l, mid)
#         mergeSort(arr, mid+1, r)
#         merge(arr, l, mid, r)


# myList = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1]
# mergeSort(myList, 0, len(myList)-1)
# print(myList)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [1, 3, 5, 2, 8, 6, 6]
mergesort(arr)


print(arr)
