n = int(input())


def wetSharkBishop(n):
    dic1 = {}
    dic2 = {}
    for _ in range(n):
        x, y = input().split()
        x, y = int(x), int(y)
        diag1, diag2 = x+y, x-y
        if diag1 in dic1:
            dic1[diag1] += 1
        else:
            dic1[diag1] = 1
        if diag2 in dic2:
            dic2[diag2] += 1
        else:
            dic2[diag2] = 1
    ans = 0
    for i in dic1.values():
        ans += (i-1)*(i)//2
    for i in dic2.values():
        ans += (i-1)*(i)//2
    return ans


print(wetSharkBishop(n))
