input = "123456"
ans = ""
quotient = 1
while True:
    if len(input) >= 6:          
        for i in input:
            i = int(i)
            while (quotient * 4) % 7 != i:
                quotient += 1
            ans += str(quotient)
            quotient = 1
    if len(ans) == 6:
        break
print(ans)