nums = list(map(int, input("輸入一組四位數字為:")))
first = nums[0]
nums[0] = nums[2]
nums[2] = first
second = nums[1]
nums[1] = nums[3]
nums[3] = second
res = ""
for i in nums:
    res += str((i+7)%10)
print(f"輸出加密後的數字為:{res}")