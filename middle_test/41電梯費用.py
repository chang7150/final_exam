time = int(input("搭了幾次電梯:"))
p = 1
res = 0
for i in range(time):
    p2 = int(input())
    if p2 > p:
        res += 20*(p2-p)
    else:
        res += 10*(p-p2)
    p = p2
print(res, "元")