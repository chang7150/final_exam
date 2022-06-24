num, i = 1, 1
m = int(input("請輸入階乘值M："))
while num < m:
    num *= i
    i += 1
print(f"超過M為{m}的最小階層N值為：{i-1}")
'''
1*2*3*4
'''