n = int(input("輸入比數n: "))
t = {}
for i in range(n):
    eg, ch = input().split()
    t[eg] = ch
s = input("輸入欲查詢單字: ")
print(f"{s}中文意思為{t[s]}")