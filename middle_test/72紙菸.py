n = int(input("請輸入N: "))
k = int(input("請輸入K: "))
butt =  n // k
secondhand_smoke = butt
judge = 0
while butt >= k:
    butt //= k
    judge += butt
ans = secondhand_smoke + judge + n
print(ans)
