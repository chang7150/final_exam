n = int(input("正數n:"))
print("數列:", n, end=" ")
while n != 1:
    if n % 2 != 0:
        n = 3*n+1
    else:
        n //= 2
    print(n, end=" ")