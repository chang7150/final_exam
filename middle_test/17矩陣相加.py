arrayA, arrayB = [], []
a, b = input().split()
for i in range(int(a)):
    arrayA.append(list(map(int, input().split())))
c, d = input().split()
for i in range(int(c)):
    arrayB.append(list(map(int, input().split())))
if a != c or b != d:
    print("兩個矩陣無法相加")
    exit()
res = []
for i in range(len(arrayA)):
    for j in range(len(arrayA[i])):
        res.append(str(arrayA[i][j] + arrayB[i][j]))

res1 = res[:len(res)//2]
res2 = res[len(res)//2:]
print(" ".join(res1))
print(" ".join(res2))