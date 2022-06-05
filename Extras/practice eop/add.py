def addArr(arr):
    num = arr[-1]+1
    arr[-1] = num % 10
    carry = num // 10
    if carry == 0:
        print(arr)
        return
    for i in reversed(range(len(arr)-1)):
        num = arr[i] + carry
        carry = num // 10
        arr[i] = num % 10
    print(arr)


addArr([0])
