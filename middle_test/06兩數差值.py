nums = input("輸入值為: ").split(",")
maxnum = "".join(sorted(nums, reverse=True))
minnum = "".join(sorted(nums))
print(f"最大值數列與最小值數列差值為：{int(maxnum)-int(minnum)}")