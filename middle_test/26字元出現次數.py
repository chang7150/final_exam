s = input("檢測的字元(end結束):")
while s != "end":
    c = input("檢測的單一字元:")
    cou = 0
    for i in s:
        if i == c:
            cou += 1
    print(f"字元{c}出現的次數為:{cou}")
    s = input("檢測的字元(end結束):")