a = input("甲方的數字：")
b = input("乙方的數字：")
res = ""
for i in range(len(a)):
    if a[i] == b[i]:
        res += "和"
    elif a[i] == "1":
        if b[i] == "5":
            res += "贏"
        else:
            res += "輸"
    elif b[i] == "1":
        if a[i] == "5":
            res += "輸"
        else:
            res += "贏"
    else:
        if int(a[i]) < int(b[i]):
            res += "輸"
        else:
            res += "贏"
print("洗刷刷結果:", res)