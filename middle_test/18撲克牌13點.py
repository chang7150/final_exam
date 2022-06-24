cards = input().split()
res = 0
for card in cards:
    if card == "A":
        res += 1
    elif card == "J":
        res += 11
    elif card == "Q":
        res += 12
    elif card == "K":
        res += 13
    else:
        res += int(card)
print(res)