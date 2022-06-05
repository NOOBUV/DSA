def firstMissingNum(arr):
    start, end = 0, len(arr)-1
    while start < end:
        if start != arr[start]:
            return start
        mid = (start+end)//2
        if mid == arr[mid]:
            start = mid+1
    return end+1


arr = [0, 1, 2, 6, 9]
m = 10
print(firstMissingNum(arr))
