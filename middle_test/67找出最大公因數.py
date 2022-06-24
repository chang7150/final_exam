nums = input("輸入數字(以，做間格)").split(",")
max_ = int(max(nums))
judge = []
for i in range(max_,0,-1):
    if max_ % i == 0:
        for j in range(len(nums)-1):
            if int(nums[j]) % i == 0:
                judge.append(i)
ans = max(judge)
print(ans)