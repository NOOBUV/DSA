arr = [int(i)
       for i in input("Enter array elements followed by space: ").split()]
num = int(input("Enter the number: "))
print(arr)


def floor(arr, num):
    floor = -1
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            floor = arr[mid]
            start = mid+1
        else:
            end = mid-1
    return floor


def ceiling(arr, num):
    ceil = -1
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            start = mid+1
        else:
            ceil = arr[mid]
            end = mid-1
    return ceil


print(floor(arr, num), ceiling(arr, num))
