price = {186:[0.09, 0.9, 0.8], 386:[0.08, 0.8, 0.7], 586:[0.07, 0.7, 0.6], 986:[0.06, 0.6, 0.5]}
ty, time = map(int, input().split(','))
res = time * price[ty][0]
if res > ty:
    res *= price[ty][2]
else:
    res *= price[ty][1]
print(round(res))