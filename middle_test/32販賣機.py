money = int(input("小明身上有幾元:"))
drink = int(input("販賣機有幾種飲料:"))
td = []
for i in range(drink):
    td.append(int(input()))
res = 0
for i in td:
    if money >= i:
        res += 1
print(res)