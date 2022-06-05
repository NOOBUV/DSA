# def partition(arr, left, right):
#     pivot = arr[left]
#     i, j = left, right
#     while i < j:
#         while i < j:
#             if arr[i] > pivot:
#                 break
#             i += 1
#         while j >= i:
#             if arr[j] <= pivot:
#                 break
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[left], arr[j] = arr[j], arr[left]
#     return j


# def quickSort(arr, left, right):
#     if left < right:
#         pivot = partition(arr, left, right)
#         quickSort(arr, left, pivot-1)
#         quickSort(arr, pivot+1, right)


# Arr = [9, 0, 2, 3, 8, 7, 4, 6]
# quickSort(Arr, 0, len(Arr)-1)
# print(Arr)

# def partition(A, index):
#     pivot = A[index]
#     i, j = index, len(A)-1
#     for i in range(len(A)):
#         for j in range(i+1, len(A)):
#             if A[j] < pivot:
#                 A[i], A[j] = A[j], A[i]
#                 break
#         print(A, " forward")
#     for i in reversed(range(len(A))):
#         if A[i] < pivot:
#             break
#         for j in reversed(range(i)):
#             if A[j] > pivot:
#                 A[i], A[j] = A[j], A[i]
#                 break
#         print(A, " reversed")

# def partition(A, index):
#     pivot = A[index]
#     smaller = 0
#     for i in range(len(A)):
#         if A[i] < pivot:
#             A[i], A[smaller] = A[smaller], A[i]
#             smaller += 1
#         print(A, " forward")
#     larger = len(A)-1
#     for i in reversed(range(len(A))):
#         if A[i] < pivot:
#             break
#         elif A[i] > pivot:
#             A[i], A[larger] = A[larger], A[i]
#             larger -= 1
#         print(A, " reversed")

# def partition(A, index):
#     pivot = A[index]
#     # Keep the following invariants during partitioning:
#     # botton group: A[:smaller].
#     # middle group: A[smaller:equal].
#     # unclassified group: A[equal:larger].
#     # top group: A[larger: ] .
#     smaller, equal, larger = 0, 0, len(A)
#     # Keep iterating as long as there is an unclassified elenent
#     while equal < larger:
#         if A[equal] < pivot:
#             A[equal], A[smaller] = A[smaller], A[equal]
#             equal, smaller = equal + 1, smaller + 1
#         elif A[equal] == pivot:
#             equal += 1
#         else:
#             larger -= 1
#             A[equal], A[larger] = A[larger], A[equal]


# arr = [1, 3, 5, 7, 8, 9, 2, 4]
# partition(arr, len(arr)-1)
# print(arr)

def partition_variation(A):
    bottom, top = 0, len(A)-1
    bottomObj, topObj = 1, 4  # given
    for bottomObj in range(bottomObj, topObj):
        if topObj < bottomObj:
            break
        equal = bottom
        while (equal <= top):
            if A[equal] == bottomObj:
                A[equal], A[bottom] = A[bottom], A[equal]
                equal, bottom = equal+1, bottom + 1
            elif A[equal] == topObj:
                A[equal], A[top] = A[top], A[equal]
                top -= 1
            else:
                equal += 1
        bottomObj, topObj = bottomObj+1, topObj-1


def partition_variation_faster(A):
    # here we will be making the ends of table seperate from middle
    bottom, top = 0, len(A)-1
    bottomObj, topObj = 1, 4  # given
    for bottomObj in range(bottomObj, topObj):
        if topObj < bottomObj:
            break

        while A[bottom] == bottomObj:
            bottom += 1
        while A[top] == topObj:
            top -= 1

        equal = bottom
        while (equal <= top):
            if A[equal] == bottomObj:
                A[equal], A[bottom] = A[bottom], A[equal]
                equal = equal+1

                while (A[bottom] == bottomObj):
                    bottom += 1

            elif A[equal] == topObj:
                A[equal], A[top] = A[top], A[equal]
                top -= 1

                while A[top] == topObj:
                    top -= 1

            else:
                equal += 1
        bottomObj, topObj = bottomObj+1, topObj-1


arr = [1, 2, 3, 4, 3, 1, 2, 3, 3, 4]
partition_variation(arr)
print(arr)
