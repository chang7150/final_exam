data = []
while True :
    x = input("請輸入代辦事項(end為停止)")
    data.append(x)
    if "end" in data:
        break
data.pop()
for i in range(1,len(data)+1):
    print(f"{i}. {data[i-1]}")

