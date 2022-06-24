eg = input("請輸入英文句子:")
l, r = 0, len(eg)-1
while eg[l] == " " or eg[l] == ".":
    l += 1
while eg[r] == " " or eg[r] == ".":
    r -= 1
eg = eg[l:r+1].split()
eg.reverse()
print(eg)