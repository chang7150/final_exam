n = int(input("輸入比數n: "))
t = {}
for i in range(n):
    a, b = input().split()
    t[a] = b
for i in t:
    print(f"{i}牌得到{t[i]}面")