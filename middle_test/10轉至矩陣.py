import numpy
n, m = input("輸入N及M為: ").split()
total = []
for i in range(int(n)):
    total.append(input(f"輸入矩陣數值第{i+1}列為:").split())
total = numpy.array(total)
total = total.T
for i in range(len(total)):
    print(f"輸入矩陣數值第{i+1}列為:", end="")
    for j in total[i]:
        print(j, end=" ")
    print()