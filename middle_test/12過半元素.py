nums = input("輸入一整數序列為: ").split()
for i in nums:
    if len(nums) % 2 == 0 and nums.count(i) >= len(nums)//2:
        print(f"過半元素為:{i}")
        exit()
    elif len(nums) % 2 != 0 and nums.count(i) > len(nums)//2:
        print(f"過半元素為:{i}")
        exit()
print("過半元素為:NO")