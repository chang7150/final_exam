num1 = str(input("輸入第一組數字(2~6位數)"))
num2 = str(input("輸入第二組數字(同第一組數字的位數)"))
a = 0
b = 0

if len(num1) < 6 or len(num1) > 2:
    for i in range(len(num1)):
        if num2[i] in num1:
            if num2[i] == num1[i]:
                a += 1
            else:
                b += 1
    if b == 0 and a != 0:
        print(f"{a}A{b}B 全對")
    else:
        print(f"{a}A{b}B 加油") 
else:
    print("數字太大或太小")