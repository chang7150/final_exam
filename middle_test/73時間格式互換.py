time = input("輸入 時:分:秒").split(":")
ans1 = (int(time[0]) * 60 + int(time[1])) * 60 + int(time[2])

second = int(input("請輸入秒數"))
t = second % 60
h = second // 60
m = 0
while True:
    if h >= 60:
        h -= 60 
        m += 1
    else:
        break
print(ans1)
print(f"{m}:{h}:{t}")
