place = []
for i in range(int(input())):
    place.append(int(input()))
for i in range(len(place)):
    if place[i] % 9 == 0 or place[i] % 11 == 0:
        print(f"第{i+1}個點 {place[i]}")