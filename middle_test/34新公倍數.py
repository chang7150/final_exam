num = int(input("請輸入一正整數:"))
if num % 2 == 0 and num % 11 == 0 and num % 5 != 0 and num % 7 != 0:
    print(f"{num}為新公倍數?:YES")
else:
    print(f"{num}為新公倍數?:NO")