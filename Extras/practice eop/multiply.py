def multiplyArr(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10
    pointer = 0
    for i in range(len(result)-1):
        if result[i] == 0:
            pointer += 1
        else:
            break
    result[pointer] *= sign
    return result[pointer:]


print(multiplyArr([1, 2], [1, 2]))
