def check(x, A, N, C):
    cows_placed, last_pos = 1, A[0]
    for i in range(1, N):
        if (A[i]-last_pos) >= x:
            cows_placed += 1
            if cows_placed == C:
                return True
            last_pos = A[i]
    return False


def aggresiveCows(A, N, C):
    A.sort()
    low, high, pos = 0, 10**9, 0
    while low <= high:
        mid = (low+high)//2
        if check(mid, A, N, C):
            low = mid+1
            pos = mid
        else:
            high = mid-1
    return pos


testcase = int(input("Entet the number of test cases: "))
for i in range(testcase):
    temp = input("Enter N following with space then C: ").split()
    temp1 = [int(i) for i in temp]
    N, C = temp1[0], temp1[1]
    A = []
    for i in range(N):
        a = int(input(f"Enter the {i}th element of the array: "))
        A.append(a)
    print(aggresiveCows(A, N, C))
