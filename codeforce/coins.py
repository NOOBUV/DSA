arr = [["A", 0], ["B", 0], ["C", 0]]
rev = {"A": 0, "B": 1, "C": 2}
for i in range(3):
    line = input()
    if line[1] == ">":
        arr[rev[line[0]]][1] += 1
    else:
        arr[rev[line[2]]][1] += 1
arr.sort(key=lambda x: x[1])
print(arr)
if arr[0][1] == arr[1][1] or arr[1][1] == arr[2][1]:
    print("Impossible")
else:
    print("".join([x[0] for x in arr]))
