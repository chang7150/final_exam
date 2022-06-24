total = []
for i in range(int(input("組數為:"))):
    all, half = input(f"第{i+1}組:").split()
    total.append(int(all)*250+int(half)*175)
for i in range(len(total)):
    print(f"第{i+1}組應收費用:{total[i]}")