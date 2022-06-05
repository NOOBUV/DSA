arr = [64, 25, 12, 22, 11]


def selectSort(arr, dec):
    for i in range(len(arr)):
        _min, _minInd = float('inf'), 0
        for j in range(i, len(arr)):
            if _min > arr[j]:
                _minInd = j
                _min = arr[j]
        arr[_minInd], arr[i] = arr[i], arr[_minInd]
    print(arr)


selectSort(arr, False)
