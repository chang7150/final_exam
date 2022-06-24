ans = input()
z = input()
a, b = 0, 0
while z != "0000":
    for i in range(len(z)):
        if z[i] in ans:
            if z[i] == ans[i]:
                a += 1
            else:
                b += 1
    print(f"{a}A{b}B")
    a, b = 0, 0
    z = input()