def areConsecutive(arr):
    n = len(arr)
    if (n < 1):
        return False
    Min = min(arr)
    Max = max(arr)
    if (Max + Min - 1 == n):
        visited = [False for i in range(n)]
        for i in range(n):
            if (visited[arr[i]-Min] != False):
                return False
            visited[arr[i]-Min] = True
        return True
    return False


print(areConsecutive([5, 4, 2, 3, 1, 6]))
