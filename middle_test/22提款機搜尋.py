info = {"123 456":"9000", "456 789":"5000", "789 888":"6000", "336 558":"10000", "775 666":"12000", "566 221":"7000"}
n = int(input("輸入查詢組數N為:"))
total = []
for i in range(n):
    ap = input()
    total.append(ap)
for i in total:
    if i in info:
        print(info[i])
    else:
        print("error")