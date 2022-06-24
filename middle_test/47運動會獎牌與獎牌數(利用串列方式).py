n = int(input("輸入比數n: "))
t = []
for i in range(n):
    a = input().split()
    t.append(a)
for i in t:
    print(f"{i[0]}牌得到{i[1]}面")