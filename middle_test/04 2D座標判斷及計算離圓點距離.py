x = int(input("X軸座標: "))
y = int(input("Y軸座標: "))
if x > 0:
    if y > 0:
        print("該點位於第一象限，", end="")
    elif y < 0:
        print("該點位於第四象限，", end="")
    else:
        print("該點位於右半平面X軸上，", end="")
elif x < 0:
    if y > 0:
        print("該點位於第二象限，", end="")
    elif y < 0:
        print("該點位於第三象限，", end="")
    else:
        print("該點位於左半平面X軸上，", end="")
else:
    if y > 0:
        print("該點位於上半平面Y軸上，", end="")
    elif y < 0:
        print("該點位於下半平面Y軸上，", end="")
    else:
        print("該點位於原點", end="")
dis = x**2+y**2
if dis:
    print(f"離原點距離為根號{dis}")