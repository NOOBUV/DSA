n = int(input())
heights = input().split()
heights = [int(x) for x in heights]
sum = 0
Min = float('inf')
for i in range(n-1):
    sum += heights[i] - heights[i+1]
    Min = min(Min,sum)
print(heights[0] - Min)
    