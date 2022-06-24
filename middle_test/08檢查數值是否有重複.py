a = int(input("輸入第一行正整數為: "))
numlist = list(map(int, input("第二行中數列中的數字為: ").split()))
numlist.sort()
i = 0
res, tmp = 1, 1
while i < len(numlist)-1:
    if numlist[i] == numlist[i+1]:
        tmp += 1
    else:
        res = max(res, tmp)
        num = numlist[i]
    i += 1
if res == 1:
    print("每個數字剛好只出現1次")
else:
    print(f"最大出現次數的數字為:{num}")
    print(f"出現最大次數為:{res}")