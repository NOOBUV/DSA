# print("hello", "world", sep=";")
# print('hi')

# def factors(n):
#     for k in range(1, n+1):
#         if n % k == 0:
#             yield k


# for i in factors(100):
#     print(i)

# infinite fibonacci series
# def fibonacci():
#     a = 0
#     b = 1
#     while True:
#         yield a
#         a, b = b, a+b


# count = 0
# for k in fibonacci():
#     print(k)
#     count += 1
#     if count == 10:
#         break

# fibonnaci with bad recursion: TC->O(2^n)
import sys


def bad_fibo(n):
    if n <= 1:
        return n
    else:
        return bad_fibo(n-1) + bad_fibo(n-2)
# fibonacci with good recursion: TC->O(n)


def good_fibo(n):
    if n <= 1:
        return (n, 0)
    else:
        a, b = good_fibo(n-1)
        return (a+b, a)

# linear sum using recursion


def linear_sum(A, n):
    if n == 0:
        return 0
    else:
        return linear_sum(A, n-1)+A[n-1]


# reversing a sequence with recusion

def reverse_seq(A, start, stop):
    if start < stop-1:
        A[start], A[stop-1] = A[stop-1], A[start]
        reverse_seq(A, start+1, stop-1)

# power function


def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x, n-1)


def imp_power(x, n):
    if n == 0:
        return 1
    else:
        partial = imp_power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


print(imp_power(2, 5))


def harmonic_number(n):
    if n <= 1:
        return 1
    return harmonic_number(n-1) + 1/n


def str_to_int(s, n, count=0):
    if n == 0:
        return 0
    return str_to_int(s, n-1, count+1) + int(s[n-1])*10**count


def Max(nums):
    l = len(nums)
    if l == 1:
        return nums[0]
    m1 = Max(nums[0:l//2])
    m2 = Max(nums[l//2:l])
    if m1 > m2:
        return m1
    else:
        return m2


def Min(nums):
    l = len(nums)
    if l == 0:
        return 0
    m1 = Max(nums[0:l//2])
    m2 = Max(nums[l//2:l])
    if m1 < m2:
        return m1
    else:
        return m2


def max_min(A, n, Max=-float('inf'), Min=float('inf')):
    if n == 0:
        return 0
    Max = max(max_min(A, n-1, Max, Min), A[n-1])
    Min = min(max_min(A, n-1, Max, Min), A[n-1])
    return Max, Min


# print(max_min([0, 1, 2, 3, 4], 4))
