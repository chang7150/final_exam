nums = input("請輸入正整數：")
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
res = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        pr = prime(int(nums[i:j+1]))
        if pr and int(nums[i:j+1]) > res:
            res = int(nums[i:j+1])
print(res)